from django.db import models


# Create your models here.
class Attendance(models.Model):
    date = models.DateField(primary_key=True)
    clock_in = models.TimeField(null=True)
    clock_out = models.TimeField(null=True)
    total_work_duration = models.TimeField(null=True)
    status = models.SlugField()
