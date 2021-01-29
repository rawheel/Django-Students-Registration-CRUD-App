from django import forms
from .models import Students
class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        labels = {
            'std_rn':'Roll No',
            'std_name':'Full Name',
            'std_contact': 'Contact',
            'std_email': 'Email'
        }

