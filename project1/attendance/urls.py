from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # root of attendance app
    path('list/', views.attendance_list, name='attendance_list'),
]