from django.db import models
from django.contrib.auth.models import User


# # Create your models here.
# class Attendance(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateField()
#     clock_in = models.TimeField(null=True)
#     clock_out = models.TimeField(null=True)
#     total_work_duration = models.TimeField(null=True)
#     status = models.SlugField()

class Attendance1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    clock_in = models.TimeField(null=True)
    clock_out = models.TimeField(null=True)
    total_work_duration = models.CharField(max_length=70,null=True)
    status = models.SlugField()