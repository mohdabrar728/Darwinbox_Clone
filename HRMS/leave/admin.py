from django.contrib import admin
from .models import LeaveModel

@admin.register(LeaveModel)
class LeaveModelAdmin(admin.ModelAdmin):
    list_display = ['select_leave_type', 'start_date_from', 'start_date_to', 'message', 'attachment']