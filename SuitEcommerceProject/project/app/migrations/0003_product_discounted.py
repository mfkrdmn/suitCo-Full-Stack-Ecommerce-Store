# Generated by Django 4.0.5 on 2022-06-26 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discounted',
            field=models.FloatField(default='1'),
        ),
    ]
