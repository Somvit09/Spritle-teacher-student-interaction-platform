from django.urls import path
from .views import login_view, register_student, register_teacher, index
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('', index, name="home"),
    path('register_student/', register_student, name="register_student"),
    path('register_teacher/', register_teacher, name="register_teacher"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path('task/', views.give_tasks, name='task'),
    path('show_task/', views.show_task, name='show_task'),
    path('submit_result/<int:pk>/', views.submit_result, name='submit_result'),
    path('check_all_result/', views.check_answers_and_show_results, name='check_all_result'),
]
