from django.contrib import admin
from .models import Department, Course, Student, Material
from .forms import StudentForm




admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Material)
