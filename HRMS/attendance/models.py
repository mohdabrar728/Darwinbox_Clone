from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(primary_key=True)
    clock_in = models.TimeField(null=True)
    clock_out = models.TimeField(null=True)
    total_work_duration = models.TimeField(null=True)
    status = models.SlugField()
