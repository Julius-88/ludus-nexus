# Generated by Django 3.2.23 on 2023-12-04 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderdetails', to='bag.order'),
        ),
    ]
