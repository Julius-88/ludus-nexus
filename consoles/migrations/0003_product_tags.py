# Generated by Django 3.2.23 on 2023-11-30 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consoles', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='consoles.Tag'),
        ),
    ]
