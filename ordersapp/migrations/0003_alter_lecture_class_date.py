# Generated by Django 3.2.5 on 2021-09-07 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0002_lecture_class_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture_class',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
