from django.db import models

# Create your models here.
class Std_details(models.Model):
    student_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    st_designation = models.CharField(max_length=100)
    study_purpose = (
        ('D', 'DNB'), ('M', 'MSc'), ('P', 'PhD'), ('O', 'Others')
    )

    # 3
    st_any_pub = models.TextField(default ="banda")
    # 2
    st_study_purpose = models.CharField(max_length=100, choices=study_purpose)

    st_study_other = models.CharField(max_length=100)
  # todo  st_collab_id = models.ForeignKey('project.collaborations', on_delete=models.CASCADE)

    status_choice = (
        (1, 'Not applied'),
        (2, 'applied'),
        (3, 'approved'),
        (4, 'rejected')
    )
    status_choice_id = models.IntegerField(choices=status_choice, default=1)

    project_status  = (
        (0,'Not Filled'),
        (1,'Guide Approval'),
        (2,'Director Review'),
        (3,'IRB Review'),
    )

    st_project_status = models.IntegerField(choices=project_status, default=0)

