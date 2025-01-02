from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from .models import Admin, Faculty, Student, Subject, Schedule
from django.urls import reverse_lazy



class HomePageView(TemplateView):
    template_name = 'app/home.html'


class AboutPageView(TemplateView):
    template_name = 'app/about.html'


class ContactsPageView(TemplateView):
    template_name = 'app/contacts.html'


class AdminListView(ListView):
    model = Admin
    context_object_name = 'Admins'
    template_name = 'app/Admin_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        return queryset

class AdminDetailView(DetailView):
    model = Admin
    context_object_name = 'Admin'
    template_name = 'app/Admin_detail.html'

class AdminCreateView(CreateView):
    model = Admin
    fields = ['AdminID', 'user', 'contact_number', 'department']
    template_name = 'app/Admin_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
class AdminUpdateView(UpdateView):
    model = Admin
    fields = ['contact_number', 'department']
    template_name = 'app/Admin_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Admin'] = self.get_object()
        return context

class AdminDeleteView(DeleteView):
    model = Admin
    template_name = 'app/Admin_delete.html'
    success_url = reverse_lazy('home')

class FacultyListView(ListView):
    model = Faculty
    context_object_name = 'Faculties'
    template_name = 'app/Faculty_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        return queryset

class FacultyDetailView(DetailView):
    model = Faculty
    context_object_name = 'Faculty'
    template_name = 'app/Faculty_detail.html'

class FacultyCreateView(CreateView):
    model = Faculty
    fields = ['FacultyID', 'user', 'department', 'hire_date']
    template_name = 'app/Faculty_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

class FacultyUpdateView(UpdateView):
    model = Faculty
    fields = ['department', 'hire_date']
    template_name = 'app/Faculty_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Faculty'] = self.get_object()
        return context

class FacultyDeleteView(DeleteView):
    model = Faculty
    template_name = 'app/Faculty_delete.html'
    success_url = reverse_lazy('home')

class StudentListView(ListView):
    model = Student
    context_object_name = 'Students'
    template_name = 'app/Student_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        return queryset

class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'Student'
    template_name = 'app/Student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    fields = ['StudentID', 'user', 'enrollment_date', 'major']
    template_name = 'app/Student_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
class StudentUpdateView(UpdateView):
    model = Student
    fields = ['enrollment_date', 'major']
    template_name = 'app/Student_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Student'] = self.get_object()
        return context

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'app/student_delete.html'
    success_url = reverse_lazy('home')

class SubjectListView(ListView):
    model = Subject
    context_object_name = 'Subjects'
    template_name = 'app/Subject_list.html'

class SubjectDetailView(DetailView):
    model = Subject
    context_object_name = 'Subject'
    template_name = 'app/Subject_detail.html'

class SubjectCreateView(CreateView):
    model = Subject
    fields = ['name', 'code', 'faculty']
    template_name = 'app/Subject_create.html'

class SubjectUpdateView(UpdateView):
    model = Subject
    fields = ['name', 'code', 'faculty']
    template_name = 'app/Subject_update.html'

class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'app/Subject_delete.html'
    success_url = reverse_lazy('home')

# Schedule Views
class ScheduleListView(ListView):
    model = Schedule
    context_object_name = 'Schedules'
    template_name = 'app/Schedule_list.html'

class ScheduleDetailView(DetailView):
    model = Schedule
    context_object_name = 'Schedule'
    template_name = 'app/Schedule_detail.html'

class ScheduleCreateView(CreateView):
    model = Schedule
    fields = ['student', 'subject', 'faculty', 'day_of_week', 'start_time', 'end_time']
    template_name = 'app/Schedule_create.html'

class ScheduleUpdateView(UpdateView):
    model = Schedule
    fields = ['student', 'subject', 'faculty', 'day_of_week', 'start_time', 'end_time']
    template_name = 'app/Schedule_update.html'

class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'app/Schedule_delete.html'
    success_url = reverse_lazy('home')
