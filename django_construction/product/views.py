from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Product
from supplier.models import Supplier
from category.models import SubCategory
from .forms import ProductCreateForm


class ProductHome(LoginRequiredMixin,View):
    def get(self, request):
        form = ProductCreateForm()
        return render(request, "product/products.html", {'form': form})
    
class ProductData(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.order_by('-created_at')
        data = []

        for counter, product in enumerate(products, start=1):
            data.append({
                'ID': counter,
                'Name': product.name,
                'Supplier': product.supplier.name,
                'SubCategory': product.sub_category.name,
                'InStock': product.in_stock,
                'UnitPrice': product.unit_price,
                'Action': f'<a class="btn-edit" data-bs-toggle="modal" data-bs-target="#addProductModal" data-pid="{product.id}"><i class="bx bxs-edit"></i></a>'
                          f'<a class="ms-3 btn-delete" data-pid="{product.id}"><i class="bx bxs-trash"></i></a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})
        

class save_productData(View):
    def post(self, request):
        pid = request.POST.get('pid', '')
        supplier = request.POST.get('supplier') 
        sub_category = request.POST.get('sub_category') 
        form = ProductCreateForm(request.POST or None, instance=None if pid == '' else Product.objects.get(id=pid))
        if form.is_valid():
            product = form.save(commit=False)
            product.supplier = get_object_or_404(Supplier,id=supplier)
            product.sub_category = get_object_or_404(SubCategory,id=sub_category)
            product.user = request.user
            product.save()

            return JsonResponse({'status': 'save'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Form data is invalid'})
        
class DeleteProduct(View):
    def delete(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return JsonResponse({"status": "success"})
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Product does not exist"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
        
class EditProduct(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            data = {
                "id": product.id,
                "name": product.name,
                "supplier": product.supplier.id,
                "sub_category": product.sub_category.id,
                "details": product.details,
                "unit_price": product.unit_price
            }
            return JsonResponse(data)
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product does not exist"})
        except Exception as e:
            return JsonResponse({"error": str(e)})