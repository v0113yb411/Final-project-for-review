from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name='home'),
    path("log_in", views.log_in, name='log_in'),
    path("course_list", views.course_list, name='course_list'),
    path("course_detail/<int:pk>",views.course_detail,name='course_detail'),
    path("create_course",views.create_course,name='create_course'),
    path("more_course",views.more_course,name='more_course'),
    path("add_course/<int:pk>",views.add_course,name='add_course'),
]
