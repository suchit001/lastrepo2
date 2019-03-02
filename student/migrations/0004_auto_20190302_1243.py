# Generated by Django 2.1.7 on 2019-03-02 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_std_details_st_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='std_details',
            name='st_project_status',
            field=models.IntegerField(choices=[(0, 'Not Filled'), (1, 'Gone for Co-Guide Approval'), (2, 'Co-guide modified'), (3, ' Gone for Guide-Approval'), (4, 'Guide modified'), (5, 'Secretary Approval'), (5, 'Gone for director approval'), (6, 'director modified'), (7, 'Director approval'), (8, 'IRB modification'), (9, 'IRB approval'), (9, 'Final review pending'), (10, 'Final review done')], default=0),
        ),
    ]
