# Generated by Django 2.2.6 on 2019-10-19 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191019_0812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='tips',
        ),
    ]
