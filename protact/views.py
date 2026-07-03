from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

def prodact_form(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('create_product') 
    return render(request, 'product-form.html', {'form': form})

def Product_list(request):
    products = Product.objects.all()
    return render(request,'products-list.html',{'products':products})

def product_view(request,id):
    product = Product.objects.get(id=id)
    return render(request,'product-view.html',{'product':product})
# from .models import Product


def prodact_uptade(request,id):
    prodact = Product.objects.get(id=id)
    form = ProductForm(request.POST or None,request.FILES or None, instance=prodact)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('products-list')
    return render(request,'product-form.html',{'form':form})

def prodact_delete(request,id):
    prodact = Product.objects.get(id=id)
    prodact.delete()
    return redirect('products-list')
# def product(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         description = request.POST.get('desciption')
#         image = request.FILES.get('image')
#         file = request.FILES.get('file')

#         # Bazaga saqlash
#         Product.objects.create(
#             name=name,
#             price=price,
#             desciption=description,
#             image=image,
#             file=file
#         )
#         return redirect('/product/')
        
#     return render(request, 'protact.html')

    