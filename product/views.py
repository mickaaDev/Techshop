from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required, \
    user_passes_test
from product.models import *
from product.forms import ProductForm



def products(request):
    context = {}
    if "query" in request.GET:
        word = request.GET.get("query")
        context["products"] = Product.objects.filter(
            Q(available=True),
            Q(deleted=False),
            Q(name__contains=word) |
            Q(description__contains=word) |
            Q(category__name__contains=word)
        )
    else:
        context["products"] = Product.objects.filter(
            available=True,
            deleted=False
        )
    return render(request, "product/products.html", context)


def product(request, id):
    context = {} 
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)


@login_required(login_url="login")
def product_create(request):
    context = {}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            new_product.user = request.user
            new_product.save()
            context["products"] = Product.objects.filter(
                available=True,
                deleted=False
            )
            context["message"] = "Товар был успешно добавлен"
            return render( request ,"product/products.html", context)

    context["form"] = ProductForm()

    return render(
        request,
        "product/form.html",
        context
    )


@login_required(login_url="login")
def product_edit(request, id):
    product = Product.objects.get(id=id)
    if request.user != product.user:
        return redirect("home")

    context = {}

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            context["product"] = Product.objects.get(id=id)
            context["message"] = "Информация успешно обновлена"
            return render(request, "product/product.html", context)

    
    context["form"] = ProductForm(instance=product)

    return render(
        request,
        "product/form.html",
        context
    )


@login_required(login_url='/login/')
def product_delete(request,id):
    product = Product.objects.get(id=id)
    context = {}

    if product.user != request.user:
        context["message"] = "У вас нет доступа!"
    else:
        product.deleted = True
        product.save()
        context["message"] = "Товар был удален"

    context["type"] = "danger"
    return render(request, "core/message,html", context)


