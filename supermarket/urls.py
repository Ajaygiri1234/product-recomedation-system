from django.urls import path
from .views import homepage,about_us,contact_us,category_content,search

#/supermarket/
urlpatterns=[

    path('1',homepage,name='homepage'),
    path('<slug:category_slug>',category_content,name='products_by_category'),
    path('search/',search,name='search'),
    path('about_us/',about_us,name='about-us'),
    path('contact_us/',contact_us,name='contact-us'),
  #  path('groceries',groceries,name='groceries'),





   ]