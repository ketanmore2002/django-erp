# Generated by Django 3.2.5 on 2021-09-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_auto_20210902_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='s_attendance',
            name='year',
            field=models.CharField(max_length=200, null=True),
        ),
    ]