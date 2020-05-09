from django import forms
from employee_register.models import Employee
class EmployeeForms(forms.ModelForm):
    class Meta:
        model=Employee
        # fields="__all__" or
        fields=("fullname","mobile","emp_code","position")

        labels={
            'fullname':"Full Name",
            'emp_code':"Employee Code",
        }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForms,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label="Select"
        self.fields['emp_code'].required=False
       
