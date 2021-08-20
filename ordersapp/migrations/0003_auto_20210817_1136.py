# Generated by Django 3.2.5 on 2021-08-17 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0002_remove_orders_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='lecture_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=20000)),
                ('subject', models.CharField(max_length=20000)),
            ],
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
