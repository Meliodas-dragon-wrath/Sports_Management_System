# Generated by Django 3.1 on 2020-11-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0005_auto_20201114_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='rule1',
            field=models.TextField(default=''),
        ),
    ]
