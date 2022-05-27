from django.db import models
from slugify import slugify
from django.urls import reverse


# Create your models here.

class company(models.Model):
    name=models.CharField(max_length=50,unique=True)
    address=models.CharField(max_length=50)
    domain=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name='company'
        verbose_name_plural='Companies'





class content(models.Model):
    company=models.ForeignKey(company,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=50)
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to='homeblog')
    offer_tag=models.CharField(max_length=50,blank=True)
    item_domain=models.CharField(max_length=200,blank=True)
    slug=models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        if not self.slug and self.item_name:
            self.slug=slugify(self.item_name)
        super(content, self).save(*args,**kwargs)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name='content'
        verbose_name_plural='Contents'



class Category(models.Model):
    category_name=models.CharField(max_length=50)
    slug=models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        if not self.slug and self.category_name:
            self.slug=slugify(self.category_name)
        super(Category, self).save(*args,**kwargs)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

