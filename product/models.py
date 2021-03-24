from django.db import models
from brand.models import Brand
from category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, editable=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        db_table = "product"