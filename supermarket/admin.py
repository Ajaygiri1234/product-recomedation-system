from django.contrib import admin
from.models import company,content,Category
# Register your models here.

class company_detail(admin.ModelAdmin):
    list_display = ['name','address','domain']

class content_detail(admin.ModelAdmin):
    list_display = ['company','item_name','category','image','offer_tag','item_domain','slug']

class categories_detail(admin.ModelAdmin):
    list_display = ['category_name','slug']


admin.site.register(company,company_detail)
admin.site.register(content,content_detail)
admin.site.register(Category,categories_detail)
