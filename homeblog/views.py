from django.shortcuts import render
from django.http import HttpResponse
from .models import products,Category

# Create your views here.


def home(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    content=products.objects.all()
    if category_slug:
        category=Category.objects.get(slug=category_slug)
        content=products.objects.filter(category=category)

    context={
        'categories': categories,
        'category': category,
        'content':content


    }
    return render(request,'homeblog/this.html',context)






