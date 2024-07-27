"""Product Views"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Product, Category
from .forms import ProductManageForm, CategoryForm



@login_required
def all_products(request):
    """A view show all products including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                if sortkey == 'category':
                    sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'


    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, "products.html", context)



@login_required
def product_detail(request, product_id):
    """A view show individual info product"""

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, "product_detail.html", context)


@login_required
def create_product(request):
    """A view to create a new product"""
    if request.method == 'POST':
        form = ProductManageForm(request.POST, request.FILES)
        category_form = CategoryForm(request.POST)  # create new category
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully.')
            return redirect('all_products')
        elif category_form.is_valid():  # Check if category form is valid
            category_form.save()
            messages.success(request, 'Category added successfully.')
            return redirect('create_product')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProductManageForm()
        category_form = CategoryForm()  

    context = {
        'form': form,
        'category_form': category_form,  
    }
    return render(request, "create_product.html", context)



@login_required
def manage_product(request, product_id):
    """ Edit the details of a gym class """
    product_manage = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        if 'save' in request.POST:
            form = ProductManageForm(request.POST, request.FILES, instance=product_manage)
            if form.is_valid():
                form.save()
                messages.success(request, 'Class updated successfully.')
                return redirect('classes_list')  # Redirect after saving
            else:
                messages.error(request, 'Check your form  something is not right.')
                return redirect('edit_class')
                
        elif 'delete' in request.POST:
            product_manage.delete()
            messages.success(request, 'Class deleted successfully.')
            return redirect('all_products')  # Redirect after deletion
        elif 'cancel' in request.POST:
            return redirect('all_products')  # Redirect on cancel

    else:
        form = ProductManageForm(instance=product_manage)

    return render(request, 'manage_product.html', {'form': form, 'product_detail': product_manage})
