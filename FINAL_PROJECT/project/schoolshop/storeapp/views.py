# from django.contrib import auth, messages
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
# from django.core.checks import messages
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import StudentForm, MaterialForm
from .models import Course, Department


# Create your views here.
def home(request):

    return render(request, 'home.html',)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('view')  # Use the URL name 'home' here
        else:
            messages.info(request, "Invalid user")
            return redirect('login')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Registration successful. You can now log in.")
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')  # Change this line to redirect to 'register'

    return render(request, 'register.html')

def view(request):

    return render(request, 'view.html')


def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            department_id = request.POST.get('department')

            # Use .first() to get a single course instance
            course_instance = Course.objects.filter(department_id=department_id).order_by('name').first()

            # Assign the single course instance to the student
            student.course = course_instance
            student.save()

            return render(request, 'confirmation.html', {'message': 'Order Confirmed'})
    else:
        form = StudentForm()

    departments = Department.objects.all()
    return render(request, 'student_form.html', {'form': form, 'departments': departments})

from django.http import JsonResponse

def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)

# def add_student(request):
#     # Your view logic goes here
#     return render(request, 'confirmation.html')




def logout(request):
    auth.logout(request)
    return redirect('/')


