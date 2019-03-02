# Generated by Django 2.1.7 on 2019-03-02 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_std_details_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='std_details',
            name='st_project_status',
            field=models.IntegerField(choices=[(0, 'Not Filled'), (1, 'Guide Approval'), (2, 'Director Review'), (3, 'IRB Review')], default=0),
        ),
    ]