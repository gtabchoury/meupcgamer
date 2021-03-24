from django.db import models
from product.models import Product
from store.models import Store
from brand.models import Brand

class ProductStore(models.Model):
    url = models.CharField(max_length=255, blank=True, editable=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, null=True)
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING, null=True)
    last_price = models.FloatField(null=True, blank=True)
    last_promotional_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.store.name+" - "+self.brand.name+" - "+self.product.name

    class Meta:
        verbose_name = "ProdutoLoja"
        verbose_name_plural = "ProdutosLojas"
        db_table = "product_store"