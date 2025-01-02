from django.db import models
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class Admin(models.Model):
    AdminID = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    success_url = reverse_lazy('Admin')

    def __str__(self):
        return self.AdminID
    def __str__(self):
        return f"Admin: {self.user.username}"

    def get_absolute_url(self):
        return reverse("Admin_detail", kwargs={"pk": self.pk})

class Faculty(models.Model):
    FacultyID = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()
    success_url = reverse_lazy('Faculty')
    def __str__(self):
        return self.FacultyID
    def __str__(self):
        return f"Faculty: {self.user.username}"
    def get_absolute_url(self):
        return reverse("Faculty_detail", kwargs={"pk": self.pk})

class Student(models.Model):
    StudentID = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    major = models.CharField(max_length=100)

    def __str__(self):
        return self.StudentID
    def __str__(self):
        return f"Student: {self.user.username}"
    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    # title = models.CharField(max_length=100)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_schedules')
    # body = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def get_absolute_url(self):
        return reverse("Schedule_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.subject.name} - {self.day_of_week} {self.start_time} to {self.end_time}"
