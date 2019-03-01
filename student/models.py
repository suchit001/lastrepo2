from django.db import models

# Create your models here.
class Std_details(models.Model):
    student_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    st_designation = models.CharField(max_length=100)
    study_purpose = (
        ('D', 'DNB'), ('M', 'MSc'), ('P', 'PhD'), ('O', 'Others')
    )
    st_any_pub = models.TextField(default ="banda")
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
