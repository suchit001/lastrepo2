# Generated by Django 2.1.7 on 2019-02-27 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_details',
            name='PI_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Principal_investigator'),
        ),
        migrations.AddField(
            model_name='project_details',
            name='Time_frame_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Time_Frame'),
        ),
        migrations.AddField(
            model_name='project_details',
            name='completion_report_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.comp_report'),
        ),
        migrations.AddField(
            model_name='project_details',
            name='feedback_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.feedback'),
        ),
        migrations.AddField(
            model_name='project_details',
            name='progress_report_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.prog_report'),
        ),
        migrations.AddField(
            model_name='project_details',
            name='st_design_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.study_design'),
        ),
        migrations.AddField(
            model_name='project_details',
            name='stud_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Std_details'),
        ),
        migrations.AddField(
            model_name='project_details',
            name='study_steps_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.study_step'),
        ),
        migrations.AddField(
            model_name='prog_report',
            name='exp_date_completion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.expected_comp'),
        ),
        migrations.AddField(
            model_name='prog_report',
            name='feed_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.feedback'),
        ),
        migrations.AddField(
            model_name='prog_report',
            name='lab_study_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.lab_study'),
        ),
        migrations.AddField(
            model_name='prog_report',
            name='paper_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.paper_presentation'),
        ),
        migrations.AddField(
            model_name='prog_report',
            name='patient_clinical_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.clinical_studies'),
        ),
        migrations.AddField(
            model_name='prog_report',
            name='protocol_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.protocol_amend'),
        ),
        migrations.AddField(
            model_name='login',
            name='Consultant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Principal_investigator'),
        ),
        migrations.AddField(
            model_name='login',
            name='Director_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Director_details'),
        ),
        migrations.AddField(
            model_name='login',
            name='Researcher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Std_details'),
        ),
        migrations.AddField(
            model_name='login',
            name='secretariat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.sec_details'),
        ),
        migrations.AddField(
            model_name='investigation2',
            name='invest2_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.project_details'),
        ),
        migrations.AddField(
            model_name='investigation1',
            name='invest1_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.project_details'),
        ),
        migrations.AddField(
            model_name='consumable',
            name='consum_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.project_details'),
        ),
        migrations.AddField(
            model_name='comp_report',
            name='ci_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Co_Investigator'),
        ),
        migrations.AddField(
            model_name='comp_report',
            name='clin_stud_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.clinical_studies'),
        ),
        migrations.AddField(
            model_name='comp_report',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Principal_investigator'),
        ),
        migrations.AddField(
            model_name='comp_report',
            name='paper_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.paper_presentation'),
        ),
        migrations.AddField(
            model_name='comp_report',
            name='protocol_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.protocol_amend'),
        ),
        migrations.AddField(
            model_name='comp_report',
            name='st_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Std_details'),
        ),
        migrations.AddField(
            model_name='capital_equip',
            name='Budget_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.project_details'),
        ),
    ]
