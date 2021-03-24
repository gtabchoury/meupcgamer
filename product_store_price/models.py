from django.db import models
from product_store.models import ProductStore

class ProductStorePrice(models.Model):
    product_store = models.ForeignKey(ProductStore, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField(null=True)
    price = models.FloatField(null=True, blank=True)
    promotional_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.date) + " - " + self.product_store.__str__()

    class Meta:
        verbose_name = "ProdutoLojaPreço"
        verbose_name_plural = "ProdutoLojaPreços"
        db_table = "product_store_price"