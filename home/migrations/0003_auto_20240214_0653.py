# Generated by Django 3.2.23 on 2024-02-14 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20231201_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventnotification',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventnotification',
            name='user',
        ),
        migrations.DeleteModel(
            name='NewsArticle',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='EventNotification',
        ),
    ]