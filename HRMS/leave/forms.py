from django import forms
from .models import LeaveModel

class LeaveForm(forms.ModelForm):
    class Meta:
        model = LeaveModel
        fields = '__all__'