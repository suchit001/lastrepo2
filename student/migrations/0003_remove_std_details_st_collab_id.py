# Generated by Django 2.1.7 on 2019-02-28 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_std_details_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='std_details',
            name='st_collab_id',
        ),
    ]
