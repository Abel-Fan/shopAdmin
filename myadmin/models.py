from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = "类目"
        verbose_name_plural = "类目"
    name = models.CharField(max_length=20,verbose_name="类目名称")
    father = models.ForeignKey('self',db_index=False,on_delete=models.CASCADE,blank=True,null=True,verbose_name="父id")
    def __str__(self):
        return self.name

# 类目规格表
class Attr(models.Model):
    class Meta:
        verbose_name = "类目规格"
        verbose_name_plural = "类目规格"
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="类目")
    name = models.CharField(max_length=20,verbose_name="规格名称")
    def __str__(self):
        return self.name


# 类目规格选项表

class AttrChoice(models.Model):
    class Meta:
        verbose_name = "类目规格选项"
        verbose_name_plural = "类目规格选项"
    attr = models.ForeignKey(Attr,on_delete=models.CASCADE,verbose_name="类目规格")
    name = models.CharField(max_length=20,verbose_name="规格选项名称")
    def __str__(self):
        return self.name


class Goods(models.Model):
    class Meta:
        verbose_name = "商品管理"
        verbose_name_plural = "商品管理"
    name = models.CharField(max_length=20,verbose_name="商品名称")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="类目")
    info = models.CharField(max_length=200,verbose_name="商品简介")
    goods_id =models.CharField(max_length=10,verbose_name="商品编码")
    img = models.ImageField(upload_to="goods",verbose_name="商品描述")

    def __str__(self):
        return self.name


# 库存规格关联表
class ExhaustedAttr(models.Model):
    exhausted = models.ForeignKey("Exhausted", on_delete=models.CASCADE)
    attr = models.ForeignKey(Attr, on_delete=models.CASCADE)
    attrchoice = models.ForeignKey(AttrChoice,on_delete=models.CASCADE,verbose_name="规格选项")

# 库存表
class Exhausted(models.Model):
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name="商品")
    attr = models.ManyToManyField(Attr,through=ExhaustedAttr)
