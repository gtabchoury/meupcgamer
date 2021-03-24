from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, editable=True)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "category"