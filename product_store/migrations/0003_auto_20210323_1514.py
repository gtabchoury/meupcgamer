# Generated by Django 3.1 on 2021-03-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_store', '0002_auto_20210323_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstore',
            name='last_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='productstore',
            name='last_promotional_price',
            field=models.FloatField(null=True),
        ),
    ]
