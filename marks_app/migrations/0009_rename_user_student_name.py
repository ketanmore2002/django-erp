# Generated by Django 3.2.5 on 2021-09-22 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks_app', '0008_auto_20210922_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='user',
            new_name='name',
        ),
    ]
