from django.urls import path
from .views import home

urlpatterns=[
    path('',home),
    path('<slug:category_slug>',home,name='category_content'),

]