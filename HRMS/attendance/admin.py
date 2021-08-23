from django.contrib import admin
from .models import Attendance1

@admin.register(Attendance1)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'clock_in', 'clock_out', 'total_work_duration', 'status']