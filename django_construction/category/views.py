from django.http import JsonResponse
from django.shortcuts import render
from .forms import CategoryCreateForm, SubCategoryCreateForm
from .models import Category, SubCategory
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator

@login_required
def CategoryHome(request):
    form = CategoryCreateForm()
    categories = Category.objects.order_by('-created_at')

    # Set the number of items per page
    items_per_page = 10
    # Create a Paginator object with the categories queryset and items per page
    paginator = Paginator(categories, items_per_page)
    # Get the current page number from the request query parameters
    page_number = request.GET.get('page')
    # Get the Page object for the current page number
    page = paginator.get_page(page_number)

    return render(request, "categories/category.html", {'form':form,'categories':categories,'page': page})



@login_required
def save_categoryData(request):
    if request.method == "POST":
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            cid = request.POST['catid']
            name = request.POST['name']
            description = request.POST['description']
            user = request.user
            if(cid == ''):
                category = Category(name=name, description=description, user=user)
            else:
                category = Category.objects.get(id=cid)
                category.name = name
                category.description = description
                category.user = user
            category.save()
            cat = Category.objects.values()  #returns a QuerySet containing dictionaries
            print(cat)
            category_data = list(cat)
            return JsonResponse({'status':'save', 'category_data':category_data})
        else:
            return JsonResponse({'status':0})


@login_required
def delete_categoryData(request):
    if request.method == "POST":
        id = request.POST.get('cid')
        print(id)
        cat = Category.objects.get(pk=id)
        cat.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


@login_required
def edit_categoryData(request):
    if request.method == "POST":
        id = request.POST.get('cid')
        print(id)
        cat = Category.objects.get(pk=id)
        category_data ={"id":cat.id, "name":cat.name, "description":cat.description}
        return JsonResponse(category_data)
    

@login_required
def SubCategoryHome(request):
    form = SubCategoryCreateForm()
    subcategories = SubCategory.objects.order_by('-created_at')

    paginator = Paginator(subcategories, 15)  # Display 3 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form' : form,
        'page_obj': page_obj,
    }

    return render(request, "categories/subcategory.html", context)


@login_required
def save_subcategoryData(request):
    if request.method == "POST":
        form = SubCategoryCreateForm(request.POST)
        if form.is_valid():
            scid = request.POST['scatid']
            category_id = request.POST['category']
            name = request.POST['name']
            description = request.POST['description']
            user = request.user
            if(scid == ''):
                category = get_object_or_404(Category, id=category_id)
                subcategory = SubCategory(category=category, name=name, description=description, user=user)
            else:
                subcategory = SubCategory.objects.get(id=scid)
                category = get_object_or_404(Category, id=category_id)
                subcategory.category = category
                subcategory.name = name
                subcategory.description = description
                subcategory.user = user
            subcategory.save()
            # Get the SubCategory objects along with the related category
            subcategories = SubCategory.objects.select_related('category').all()
            subcategory_data = []
            for subcat in subcategories:
                data = {
                    'id': subcat.id,
                    'category': subcat.category.name,  # Access the category name
                    'name': subcat.name,
                    'description': subcat.description,
                    'status': subcat.status,
                }
                subcategory_data.append(data)
            return JsonResponse({'status':'save', 'subcategory_data':subcategory_data})
        else:
            return JsonResponse({'status':0})
        
    
@login_required
#@permission_required('category.delete_subcategory', raise_exception=True)
def delete_subcategoryData(request):
    if request.method == "POST":
        id = request.POST.get('scid')
        print(id)
        scat = SubCategory.objects.get(pk=id)
        scat.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
    

@login_required
def edit_subcategoryData(request):
    if request.method == "POST":
        id = request.POST.get('scid')
        print(id)
        scat = SubCategory.objects.get(pk=id)
        subcategory_data ={
            "id":scat.id,
            "category":scat.category.id, 
            "name":scat.name, 
            "description":scat.description
        }

        return JsonResponse(subcategory_data)
    