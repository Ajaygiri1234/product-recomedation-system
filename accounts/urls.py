from django.urls import path
from .views import sign_up,login_form,logout

# /accounts
urlpatterns = [

    path('sign_up', sign_up, name='sign_up'),
    path('login/', login_form.as_view(), name='login'),
    path('logout/', logout.as_view(), name='logout'),



]
