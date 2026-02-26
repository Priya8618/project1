from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} ({self.roll_number})"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status_choices = [
        ('Present', 'Present'),
        ('Absent', 'Absent')
    ]
    status = models.CharField(max_length=10, choices=status_choices)
    class Meta:
        unique_together = ('student', 'date')
    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"