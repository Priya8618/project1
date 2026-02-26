from django.shortcuts import render

from .models import Attendance


def home(request):
    return render(request, 'attendance/home.html')

def attendance_list(request):
    records = Attendance.objects.all().order_by('-date')
    return render(request, 'attendance/attendance_list.html', {'records': records})