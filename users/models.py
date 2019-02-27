from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    TYPE_CHOICES = (
        (0,'DIRECTOR'),
        (1,'SECRETARIAT'),
        (2,'GUIDE'),
        (3,'STUDENT'),
    )
    name = models.CharField(max_length=250,default='suchit')
    type = models.IntegerField(choices=TYPE_CHOICES, default=3)
    contact = models.IntegerField(default=100)

    def _str_(self):
        return str(self.username)
#
# class Guide(models.Model):
#     guide_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     guide_subject = models.CharField(max_length=100,default='maths')
#
#     def __str__(self):
#         return str(self.guide_id)
#
#
# class Student(models.Model):
#     student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='customstudent')
#     guide = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='customguide')
#
#     def __str__(self):
#         return str(self.student_id)



class sec_details(models.Model):

    designation = models.CharField(max_length=100)
    sec_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
         return str(self.sec_id)

class Director_details(models.Model):
    director_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)

    def __str__(self):
         return str(self.director_id)

class Std_details(models.Model):
    student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    st_designation = models.CharField(max_length=100)
    study_purpose = (
        ('D', 'DNB'), ('M', 'MSc'), ('P', 'PhD'), ('O', 'Others')
    )
    st_any_pub = models.TextField()
    st_study_purpose = models.CharField(max_length=100, choices=study_purpose)
    st_study_other = models.CharField(max_length=100)
    st_collab_id = models.ForeignKey('dashboard.collaborations', on_delete=models.CASCADE)

class Principal_investigator(models.Model):
    P_Dept = models.CharField(max_length=100)
    P_designation = models.CharField(max_length=100)
    principal_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
         return str(self.principal_id)
