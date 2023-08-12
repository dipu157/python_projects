from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from io import BytesIO
import xlwt
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.db.models import Sum

from .models import Contractor,Site
from company.models import Company
from purchase.models import Purchase
from .forms import ContractorCreateForm,SiteCreateForm,SiteEditForm


class ContractorHome(LoginRequiredMixin,View):
    def get(self, request):
        form = ContractorCreateForm()
        return render(request, "construction/contractor/contractor.html", {'form': form})
    

class ContractorData(LoginRequiredMixin, View):
    def get(self, request):
        contractors = Contractor.objects.order_by('-created_at')
        data = []

        for counter, contractor in enumerate(contractors, start=1):
            if contractor.image:
                photo_url = request.build_absolute_uri(contractor.image.url)
            else:
                photo_url = ''
            data.append({
                'ID': counter,
                'Name': contractor.name,
                'Email': contractor.email,
                'Phone': contractor.phone,
                'NID': contractor.nid,
                'Type': contractor.contractor_type,
                'Photo': photo_url,
                'Action': f'<a class="btn-edit" data-bs-toggle="modal" data-bs-target="#addContractorModal" data-conid="{contractor.id}"><i class="bx bxs-edit"></i></a>'
                          f'<a class="ms-3 btn-delete" data-conid="{contractor.id}"><i class="bx bxs-trash"></i></a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})
        
class save_contractorData(View):
    def post(self, request):
        conid = request.POST.get('conid', '')
        form = ContractorCreateForm(request.POST, request.FILES, instance=None if conid == '' else Contractor.objects.get(id=conid))
        if form.is_valid():
            contractor = form.save(commit=False) 
            contractor.company = get_object_or_404(Company, id=1)
            contractor.user = request.user
            contractor.save()

            return JsonResponse({'status': 'save'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Form data is invalid'})
        

class DeleteContractor(View):
    def delete(self, request, contractor_id):
        try:
            contractor = Contractor.objects.get(id=contractor_id)
            contractor.delete()
            return JsonResponse({"status": "success"})
        except Contractor.DoesNotExist:
            return JsonResponse({"status": "error", "message": "contractor does not exist"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
        
class EditContractor(View):
    def get(self, request, supplier_id):
        try:
            contractor = Contractor.objects.get(id=supplier_id)
            data = {
                "id": contractor.id,
                "name": contractor.name,
                "email": contractor.email,
                "phone": contractor.phone,
                "address": contractor.address,
                "nid": contractor.nid,
                "contractor_type": contractor.contractor_type,
                "image": contractor.image.url,
            }
            return JsonResponse(data)
        except Contractor.DoesNotExist:
            return JsonResponse({"error": "Contractor does not exist"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
        



class SiteHome(LoginRequiredMixin,View):
    def get(self, request):
        cform = SiteCreateForm()
        uform = SiteEditForm()
        return render(request, "construction/project_site/site.html", {'cform': cform, 'uform': uform})
    
class SiteData(LoginRequiredMixin, View):
    def get(self, request):
        sites = Site.objects.order_by('-created_at')
        data = []

        for counter, site in enumerate(sites, start=1):
            if site.image:
                photo_url = request.build_absolute_uri(site.image.url)
            else:
                photo_url = ''
            data.append({
                'ID': counter,
                'Contractor': site.contractor.name,
                'Name': site.name,
                'Area': site.area,
                'Land Owner': site.land_owner_name + "<br/>"+ site.owner_mobile,
                'Flat': "Flat: "+site.flat_qty+"<br/> Parking: "+site.parking_qty,
                'Date': site.end_date,
                'Photo': photo_url,
                'Action': f'<a class="btn-edit" data-bs-toggle="modal" data-bs-target="#editSiteModal" data-sid="{site.id}"><i class="bx bxs-edit"></i></a>'
                          f'<a class="ms-3 btn-delete" data-sid="{site.id}"><i class="bx bxs-trash"></i></a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})
        
class CreateSite(View):
    def post(self, request):
        contractor = request.POST.get('contractor')
        form = SiteCreateForm(request.POST, request.FILES)
        if form.is_valid():
            site = form.save(commit=False) 
            site.company = get_object_or_404(Company, id=1)
            site.contractor = get_object_or_404(Contractor, id=contractor)
            site.user = request.user
            site.save()

            return JsonResponse({'status': 'save'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'message': errors})
        
class DeleteSite(View):
    def delete(self, request, site_id):
        try:
            site = Site.objects.get(id=site_id)
            site.delete()
            return JsonResponse({"status": "success"})
        except Site.DoesNotExist:
            return JsonResponse({"status": "error", "message": "site does not exist"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
        

class EditSite(View):
    def get(self, request, site_id):
        try:
            site = Site.objects.get(id=site_id)
            data = {
                "id": site.id,
                "contractor": site.contractor.id,
                "name": site.name,
                "district": site.district,
                "area": site.area,
                "address": site.address,
                "details": site.details,
                "land_owner_name": site.land_owner_name,
                "owner_mobile": site.owner_mobile,
                "flat_qty": site.flat_qty,
                "parking_qty": site.parking_qty,
                "start_date": site.start_date,
                "end_date": site.end_date,
                "image": site.image.url,
            }
            return JsonResponse(data)
        except Site.DoesNotExist:
            return JsonResponse({"error": "Site does not exist"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
        

class UpdateSite(View):
    def post(self, request):
        siteid = request.POST.get('siteid')
        contractor = request.POST.get('contractor')
        site = Site.objects.get(id=siteid)  # Get the existing site instance
        form = SiteEditForm(request.POST, request.FILES, instance=site) 
        if form.is_valid():
            site = form.save(commit=False) 
            site.company = get_object_or_404(Company, id=1)
            site.contractor = get_object_or_404(Contractor, id=contractor)
            site.user = request.user
            site.save()

            return JsonResponse({'status': 'update'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'message': errors})
        

class SiteReportIndex(View):
    def get(self, request):
        sites = Site.objects.filter(company=1)
        return render(request, "construction/project_site/report/siteReportIndex.html",{'sites':sites})
    

class DateRangeSiteReport(View):
    def get(self, request):
        if request.GET.get('action'):
            from_date = request.GET.get('from_date')
            to_date = request.GET.get('to_date')
            sites = request.GET.get('site_id')
            site = Site.objects.filter(id=sites).first()
            purchases = Purchase.objects.filter(site=sites,purchase_date__range=(from_date, to_date))
            total_amount = purchases.aggregate(total=Sum('net_payable'))['total'] or 0
            context = {
                'purchases': purchases,
                'from_date': from_date,
                'to_date': to_date,
                'site': site,
                'total_amount': total_amount,
            }

            if request.GET.get('action') == 'print':
                # Render the HTML template as a string
                template = get_template("construction/project_site/report/dateRangeSiteReport.html")
                html_string = template.render(context)
                # Create a PDF object
                pdf = BytesIO()
                # Generate the PDF from the HTML content
                pisa.CreatePDF(html_string, dest=pdf)
                # Set response headers for PDF display
                response = HttpResponse(pdf.getvalue(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="site_report.pdf"'
                return response
            
            elif request.GET.get('action') == 'export':
                # Create a workbook and add a worksheet
                response = HttpResponse(content_type='application/ms-excel')
                response['Content-Disposition'] = 'attachment; filename="site_report.xls"'
                wb = xlwt.Workbook(encoding='utf-8')
                ws = wb.add_sheet('Site Report')

                # Write the header content to the worksheet
                header_content = """
                ABC Construction

                77/A, East Rajabazar,
                West Panthapath, Dhaka-1215

                Site Purchase Report From {from_date} to {to_date}
                Site Name: {site}
                """.format(from_date=from_date, to_date=to_date, site=site)
                
                header_style = xlwt.easyxf('font: bold True;')
                ws.write_merge(0, 6, 0, 4, header_content, header_style)
                
                # Write header row
                header_row = ['SL', 'Purchase Date', 'Purchase Code', 'Supplier', 'Amount']
                for col_num, header in enumerate(header_row):
                    ws.write(7, col_num, header, header_style)

                # Write data rows
                for row_num, purchase in enumerate(purchases, start=8):
                    ws.write(row_num, 0, row_num - 7)  # Adjust the row numbering
                    ws.write(row_num, 1, str(purchase.purchase_date))
                    ws.write(row_num, 2, purchase.invoice_no)
                    ws.write(row_num, 3, purchase.supplier.name)
                    ws.write(row_num, 4, purchase.net_payable)

                wb.save(response)
                return response
            
            else:
                return render(request, "construction/project_site/report/dateRangeSiteReport.html",
                              {'purchases': purchases,'from_date': from_date,'to_date': to_date,'site': site,'total_amount': total_amount,})