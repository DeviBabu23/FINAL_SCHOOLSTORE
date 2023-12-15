from django import forms
from .models import Student, Material

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'




class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'




