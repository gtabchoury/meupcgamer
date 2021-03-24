from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255, blank=True, editable=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        db_table = "brand"