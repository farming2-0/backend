# Generated by Django 2.2.6 on 2019-10-19 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20191019_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='tips',
            field=models.ManyToManyField(to='main.Tip'),
        ),
    ]
