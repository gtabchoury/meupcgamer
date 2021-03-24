from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255, blank=True, editable=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Loja"
        verbose_name_plural = "Lojas"
        db_table = "store"