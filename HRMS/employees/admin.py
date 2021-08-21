from django.contrib import admin
from .models import EmployeeDetails
# Register your models here.
@admin.register(EmployeeDetails)
class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'designation', 'department', 'email_id', 'location']