from django.db import models


# Create your models here.
class EmployeeDetails(models.Model):
    name = models.CharField(max_length=100)
    choice = [('Trainee Software Engineer', 'Trainee Software Engineer'),
              ('Trainer', 'Trainer')]
    designation = models.CharField(max_length=100, choices=choice)
    department = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    location = models.CharField(max_length=200)
