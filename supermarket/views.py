from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage

from .models import content,company,Category


# Create your views here.
def homepage(request):
    categories= Category.objects.all()
    post = content.objects.all()
    companies=company.objects.all()
    p=Paginator(post,3)
    page_num=request.GET.get('page')
    try:
        page=p.page(page_num)
    except:
        page=p.page(1)


    return render(request, 'supermarket/home.html', {'post':post, 'categories':categories, 'companies':companies,'page':page})

def category_content(request,category_slug=None):
    post=content.objects.all()
    category = None
    categories=Category.objects.all()
    if category_slug:
        category=Category.objects.get(slug=category_slug)
        post=content.objects.filter(category=category)



    return render(request, 'supermarket/household.html', {'category': category,'categories':categories, 'post': post})


def search(request):
    categories=Category.objects.all()
    query=request.GET.get('q')
    results=content.objects.filter(Q(item_name__icontains=query)|Q(company__name=query))
    print(results)
    return render(request,'supermarket/search.html',{'query':query,'results':results,'categories':categories})







def about_us(request):
    categories = Category.objects.all()
    return render(request,'supermarket/about.html',{'categories':categories,})


def contact_us(request):
    categories = Category.objects.all()
    return render(request, 'supermarket/contact.html', {'categories': categories, })







