# Generated by Django 3.2.5 on 2021-09-25 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks_app', '0018_first_year_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='first_year_student',
            name='year',
            field=models.CharField(default='1', max_length=20000, null=True),
        ),
    ]
