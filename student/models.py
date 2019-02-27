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
    st_collab_id = models.ForeignKey('student.collaborations', on_delete=models.CASCADE)


class Budget(models.Model):
    Nop = models.IntegerField()
    Travel_allow = models.IntegerField()
    No_of_visit = models.IntegerField()
    Rs_per_visit = models.IntegerField()
    Research_fellow_choices = (
        (1, 'In-house'),
        (2, 'New'),
        (3, 'DNB')
    )
    Research_fellow_id = models.IntegerField(choices = Research_fellow_choices)
    Remarks = models.TextField(blank=True)
    Miscellan = models.IntegerField()





class collaborations(models.Model):
    Institue = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Collab_type = models.TextField()
    Ec_approval = models.BooleanField(max_length=2)
    Authorship = models.TextField()
