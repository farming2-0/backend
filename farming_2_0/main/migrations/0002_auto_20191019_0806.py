# Generated by Django 2.2.6 on 2019-10-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crop',
            old_name='sid',
            new_name='cid',
        ),
        migrations.AlterField(
            model_name='machine',
            name='rent',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
