from django import forms 
from .models import Student2


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student2
        fields = '__all__'
        # exclude = ['student_bio']

# class StudentForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()
#     phone_number = forms.CharField()
#     dob = forms.DateField()
#     fathers_name = forms.CharField()


