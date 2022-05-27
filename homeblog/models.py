from django.db import models
from slugify import slugify
from django.urls import reverse


class products(models.Model):
    item_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)



class Category(models.Model):
    name=models.CharField(max_length=20)
    slug=models.SlugField(max_length=20,blank=True,null=True)

    def save(self,*args,**kwargs):
        if not self.slug and self.name:
            self.slug=slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    def _get_absolute_url(self):
        return reverse('homeblog:content_category',args=[self.slug],)