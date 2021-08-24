from django import forms


class EmployeeDetailsForms(forms.Form):
    search_by_employee_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search By Employee Name'}))
