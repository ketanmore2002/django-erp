# Generated by Django 3.2.5 on 2021-08-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0008_auto_20210818_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture_class',
            name='division',
            field=models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')], max_length=20000),
        ),
    ]
