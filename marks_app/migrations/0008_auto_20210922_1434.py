# Generated by Django 3.2.5 on 2021-09-22 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marks_app', '0007_rename_exam_exams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exams',
            name='marks',
        ),
        migrations.AddField(
            model_name='student_main',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='marks_app.exams'),
        ),
        migrations.AlterField(
            model_name='student_main',
            name='marks',
            field=models.IntegerField(null=True),
        ),
    ]
