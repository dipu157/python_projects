from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
import random
from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.db import transaction

from .forms import PurchaseForm
from product.models import Product
from company.models import Company
from construction.models import Site
from .models import Purchase,PurchaseDetails
from  supplier.models import Supplier,Supplier_Ledger,SupplierAccount,SupplierPayment


class PurchaseHome(LoginRequiredMixin,View):
    def get(self, request):
        form = PurchaseForm()
        return render(request, "purchase/purchase.html", {'form': form})
    

class ProductBySupplierId(View):
    def get(self, request):
        supplier_id = request.GET.get('id')
        products = Product.objects.filter(supplier=supplier_id)

        html = ""
        for product in products:
            html += f"""
            <tr>
                <td>
                    <input type='hidden' class='form-control product' id='productId' name='id[]' readonly value='{product.id}'>
                    <input type='text' class='form-control' name='name[]' readonly value='{product.name}'>
                </td>
                <td> <input type='text' class='form-control' name='in_stock[]' placeholder='0.00' readonly value='{product.in_stock}'> </td>
                <td><input type='text' class='form-control qty' name='qty[]' placeholder='0.00' value=''></td>
                <td><input type='text' class='form-control unit_price' name='price[]' placeholder='0.00' value='{product.unit_price}'></td>
                <td><input type='text' class='form-control uvat' name='vat[]' placeholder='0.00' value='0'></td>
                <td><input type='text' class='form-control udiscount' name='discount[]' placeholder='0.00' value='0'></td>
                <td><input type='text' class='form-control total' name='net_amount[]' placeholder='0.00' readonly value=''></td>

                <input type='hidden' class='form-control tamount' name='net_tp[]' placeholder='0.00' value='0'>
                <input type='hidden' class='form-control tvat' name='net_vat[]' placeholder='0.00' value='0'>
                <input type='hidden' class='form-control tdiscount' name='net_discount[]' placeholder='0.00' value='0'>
            </tr>
            """

        return HttpResponse(html)

class SavePurchaseData(View):
    def post(self, request, *args, **kwargs):
        supplier_id = int(request.POST.get('supplier'))
        site_id = int(request.POST.get('site'))
        supplier = get_object_or_404(Supplier, id=supplier_id)
        site = get_object_or_404(Site, id=site_id)
        company = get_object_or_404(Company, id=1)

        data = {
            'company': company,
            'purchase_code': 'P' + str(random.randint(1000, 2000)),
            'supplier': supplier,
            'site': site,
            'invoice_no': request.POST.get('invoice_no'),
            'purchase_date': request.POST.get('purchase_date'),
            'detail': request.POST.get('detail'),
            'total_amount': request.POST.get('total_amount'),
            'total_vat': request.POST.get('total_vat'),
            'total_discount': request.POST.get('total_discount'),
            'net_payable': request.POST.get('net_payable'),
            'user_id': request.user.id,
        }

        try:
            with transaction.atomic():
                invoice_id = Purchase.objects.filter(invoice_no=data['invoice_no']).values_list('invoice_no', flat=True)
                if data['invoice_no'] in invoice_id:
                    response_data = {
                        'status': 'error',
                        'message': 'This Invoice is Already exist',
                    }
                    return JsonResponse(response_data)

                supplier_balance = Supplier_Ledger.objects.filter(supplier=supplier).first()

                if not supplier_balance:
                    response_data = {
                        'status': 'error',
                        'message': 'Supplier Balance Not Found!',
                    }
                    return JsonResponse(response_data)

                net_payable = Decimal(data['net_payable'])
                paid_amount = Decimal(request.POST.get('paid_amount'))
                total_due = Decimal(request.POST.get('total_due'))

                total = supplier_balance.total_amount + net_payable
                paid = supplier_balance.paid + paid_amount
                due = supplier_balance.due + total_due

                supplier_balance_data = {
                    'total_amount': total,
                    'paid': paid,
                    'due': due
                }

                Supplier_Ledger.objects.filter(id=supplier_balance.id).update(**supplier_balance_data)

                purchase_insert = Purchase.objects.create(
                    company=data['company'],
                    purchase_code=data['purchase_code'],
                    supplier=data['supplier'],
                    site=data['site'],
                    invoice_no=data['invoice_no'],
                    purchase_date=data['purchase_date'],
                    detail=data['detail'],
                    total_amount=data['total_amount'],
                    total_vat=data['total_vat'],
                    total_discount=data['total_discount'],
                    net_payable=data['net_payable'],
                    user_id=data['user_id'],
                )

                if not purchase_insert:
                    response_data = {
                        'status': 'error',
                        'message': 'Purchase Insert Error!',
                    }
                    return JsonResponse(response_data)

                purchase_last = Purchase.objects.filter(company=company).latest('id')

                supplier_payment_data = {
                    'company': company,
                    'purchase': get_object_or_404(Purchase, id=purchase_last.id),
                    'supplier': supplier,
                    'payment_type': request.POST.get('payment_type'),
                    'issue_date': request.POST.get('issue_date'),
                    'receiver_name': request.POST.get('receiver_name'),
                    'receiver_phone': request.POST.get('receiver_contact'),
                    'paid_amount': request.POST.get('paid_amount'),
                    'user_id': request.user.id,
                }

                supplier_payment_insert = SupplierPayment.objects.create(**supplier_payment_data)

                if not supplier_payment_insert:
                    response_data = {
                        'status': 'error',
                        'message': 'Supplier Payment Insert Error!',
                    }
                    return JsonResponse(response_data)

                supplier_account_data = {
                    'company': company,
                    'purchase': get_object_or_404(Purchase, id=purchase_last.id),
                    'supplier': supplier,
                    'total_amount': request.POST.get('total_amount'),
                    'paid_amount': request.POST.get('paid_amount'),
                    'due': request.POST.get('total_due'),
                    'user_id': request.user.id,
                }

                supplier_account_insert = SupplierAccount.objects.create(**supplier_account_data)

                if not supplier_account_insert:
                    response_data = {
                        'status': 'error',
                        'message': 'Supplier Account Insert Error!',
                    }
                    return JsonResponse(response_data)

                qty_list = request.POST.getlist('qty[]')
                if not qty_list:
                    response_data = {
                        'status': 'error',
                        'message': 'Product Qty Not Filled or Processing Errror!',
                    }
                    return JsonResponse(response_data)
                for row, qtys in enumerate(qty_list):
                    if qtys:
                        qty = int(qtys)
                        product = request.POST.getlist('id[]')[row]
                        price = float(request.POST.getlist('price[]')[row])
                        vat = float(request.POST.getlist('vat[]')[row])
                        discount = float(request.POST.getlist('discount[]')[row])
                        net_amount = float(request.POST.getlist('net_amount[]')[row])

                        PurchaseDetails.objects.create(
                            company=company,
                            purchase=get_object_or_404(Purchase, id=purchase_last.id),
                            product=get_object_or_404(Product, id=product),
                            supplier=supplier,
                            site=site,
                            qty=qty,
                            price=price + vat - discount,
                            vat=vat,
                            discount=discount,
                            net_amount=net_amount,
                            user_id=request.user.id,
                        )

                        product = Product.objects.filter(id=product).first()
                        instock = product.in_stock + qty
                        unit_price = product.unit_price

                        product_data = {
                            'in_stock': instock,
                            'unit_price': unit_price,
                            'user_id': request.user.id,
                        }

                        productUpdate = Product.objects.filter(id=product.id).update(**product_data)
                        if not productUpdate:
                            response_data = {
                                'status': 'error',
                                'message': 'Product Update Errror!',
                            }
                            return JsonResponse(response_data)

            response_data = {
                'status': 'success',
                'message': 'Data successfully processed!',
            }
            return JsonResponse(response_data)

        except Exception as e:
            response_data = {
                'status': 'error',
                'message': str(e),  # You can customize the error message as needed
            }
            return JsonResponse(response_data)

class purchaseListData(View):
    def get(self, request):
        all_purchase = Purchase.objects.filter(company=1).order_by('-created_at')
        return render(request,"purchase/purchaseList.html",{'purchases':all_purchase})

