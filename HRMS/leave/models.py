from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LeaveModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    my_choice = [('causal leave','Causal Leave'), ('loss of pay','Loss Of Pay'), ('sick leave','Sick Leave')]
    select_leave_type = models.CharField(choices=my_choice, max_length=50)
    start_date_from = models.DateField()
    start_date_to = models.DateField()
    message = models.TextField()
    attachment = models.FileField(null=True)
