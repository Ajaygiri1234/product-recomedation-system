from django.shortcuts import render
from django.http import HttpResponse
import random
import pandas as pd

# Create your views here.
from django.contrib.auth.models import User


def create_user(request):
    userid = pd.read_csv('http://127.0.0.1:8000/media/user_id.csv')

    # print(userid.to_numpy())
    print(len(userid))
    for i in range(0, len(userid)):
        form = User.objects.create_user(id=userid['user_id'][i],
                                        username=(userid['first_name'][i] + str(userid['user_id'][i])),
                                        email=userid['first_name'][i] + str(userid['user_id'][i]) + "@a6mail.net",
                                        password="girigiri", first_name=userid['first_name'][i],
                                        last_name=userid['last_name'][i])
        form.save()

    return HttpResponse("successfully added")


import random
from supermarket.models import content, Category, company


def check(request):
    df = pd.read_csv('http://127.0.0.1:8000/media/product_discription1.csv')

    # print(userid.to_numpy())
    print(len(df))
    # for i in range(0, len(discription)):
    # j = Category.objects.all()[1,2,3,4,5]
    # k = company.objects.all()#[1,2,5,6,7]

    #    print()

    # for i in j:
    #   print((i.id))
    # for i in k:
    #   print(i.id)

    # j = Category.objects.get(id=1)
    # k=company.objects.get(id=1)
    for i in range(0, len(df)):
        print(i)
        try:
            form = content.objects.create(id=df['StockCode'][i],
                                      company=company.objects.get(id=random.choice([1, 2, 5, 6, 7])),
                                      item_name=df["Description"][i],
                                      category=Category.objects.get(id=random.choice([1, 2, 3, 4, 5])),
                                      image=df["Image_url"][i], offer_tag="50%off")
        except:
            pass

    # form.save()

    return HttpResponse("successfully added")
