from django.db import models

# Create your models here.


class Consumable(models.Model):
    consum_id = models.ForeignKey(to = 'project.project_details', on_delete=models.CASCADE)
    consum_name = models.CharField(max_length=250)
    qty = models.IntegerField()
    Rs_per_unit = models.IntegerField()
    Catlog_no = models.IntegerField()
    Name_of_manufact = models.CharField(max_length=250)
    Total3 = models.IntegerField(default=9)


class Investigation2(models.Model):
    invest2_id = models.ForeignKey(to = 'project.project_details', on_delete=models.CASCADE)
    tests = models.CharField(max_length=250)
    exist_test_choice = (
        (1, 'yes'),
        (2, 'no')
    )
    exist_test_id = models.IntegerField(choices=exist_test_choice)
    No_of_pat = models.IntegerField()
    Followup = models.IntegerField()
    Tarrif = models.IntegerField()
    Total2 = models.IntegerField(default=19)


class Investigation1(models.Model):
    invest1_id = models.ForeignKey(to = 'project.project_details', on_delete=models.CASCADE)
    tests = models.CharField(max_length=250)
    exist_test_choice = (
        (1, 'yes'),
        (2, 'no')
    )
    exist_test_id = models.IntegerField(choices=exist_test_choice)
    No_of_pat = models.IntegerField()
    Tarrif = models.IntegerField()
    Total1 = models.IntegerField(default=10)


class Capital_equip(models.Model):
    Budget_id = models.ForeignKey(to = 'project.project_details', on_delete=models.CASCADE)
    Name = models.CharField(max_length=250)
    Price = models.IntegerField()


class Salaryy(models.Model):
    Salary_id = models.ForeignKey(to = 'project.project_details', on_delete=models.CASCADE)
    Name = models.CharField(max_length=250)
    Study = models.IntegerField()
    Salary = models.IntegerField()
    Total0 = models.IntegerField(default=10)


