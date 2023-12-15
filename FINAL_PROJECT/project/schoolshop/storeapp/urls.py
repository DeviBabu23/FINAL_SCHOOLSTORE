from django.urls import path

from storeapp import views


urlpatterns = [

    path('', views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('view/', views.view, name='view'),
    path('student/', views.student_form, name='student_form'),
    # path('add_student/', views.add_student, name='add_student'),
    path('logout/', views.logout, name='logout'),
    path('get_courses/', views.get_courses, name='get_courses'),
]