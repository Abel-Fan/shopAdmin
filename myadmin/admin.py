from django.contrib import admin
from .models import Category,Attr,AttrChoice,Goods,Exhausted
from django.utils.html import format_html

def get_con(obj):
    if obj.father == None:
        return obj.name
    return obj.name +"<"+ get_con(Category.objects.filter(id=obj.father_id).first())


# Register your models here.
from .models import Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','get_name','get_father')
    def get_father(self,obj):
        return str(obj.father_id)
    def get_name(self,obj):
        return get_con(obj)

@admin.register(Attr)
class AttrAdmin(admin.ModelAdmin):
    list_display = ('id','name','category')

@admin.register(AttrChoice)
class AttrChoiceAdmin(admin.ModelAdmin):
    list_display = ('id','name','attr')

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id','get_img','category','name','info')
    def get_img(self,obj):
        return format_html("<img src='/static/%s' width='100' height='50'>"%obj.img)

@admin.register(Exhausted)
class ExhaustedAdmin(admin.ModelAdmin):
   pass