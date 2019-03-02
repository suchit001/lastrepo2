# Generated by Django 2.1.7 on 2019-03-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Std_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_designation', models.CharField(max_length=100)),
                ('st_any_pub', models.TextField(default='banda')),
                ('st_study_purpose', models.CharField(choices=[('D', 'DNB'), ('M', 'MSc'), ('P', 'PhD'), ('O', 'Others')], max_length=100)),
                ('st_study_other', models.CharField(max_length=100)),
                ('status_choice_id', models.IntegerField(choices=[(1, 'Not applied'), (2, 'applied'), (3, 'approved'), (4, 'rejected')], default=1)),
            ],
        ),
    ]
