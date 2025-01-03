from django.urls import path
from .views import (HomePageView, AboutPageView, ContactsPageView, ScheduleListView,
                    ScheduleDetailView, ScheduleCreateView, ScheduleUpdateView, ScheduleDeleteView,
                    AdminListView, AdminDetailView, AdminCreateView, AdminUpdateView,
                    AdminDeleteView, StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView,
                    StudentDeleteView, FacultyListView,FacultyDetailView, FacultyCreateView, FacultyUpdateView,
                    FacultyDeleteView, SubjectListView, SubjectDetailView, SubjectCreateView, SubjectUpdateView,
                    SubjectDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('SchedulePage/', ScheduleListView.as_view(), name='Schedule'),
    path('SchedulePage/<int:pk>', ScheduleDetailView.as_view(), name='Schedule_detail'),
    path('SchedulePage/create', ScheduleCreateView.as_view(), name='Schedule_create'),
    path('SchedulePage/<int:pk>/edit', ScheduleUpdateView.as_view(), name='Schedule_update'),
    path('SchedulePage/<int:pk>/delete', ScheduleDeleteView.as_view(), name='Schedule_delete'),
    path('AdminPage/', AdminListView.as_view(), name='Admin'),
    path('AdminPage/<int:pk>', AdminDetailView.as_view(), name='Admin_detail'),
    path('AdminPage/create', AdminCreateView.as_view(), name='Admin_create'),
    path('AdminPage/<int:pk>/edit', AdminUpdateView.as_view(), name='Admin_update'),
    path('AdminPage/<int:pk>/delete', AdminDeleteView.as_view(), name='Admin_delete'),
    path('StudentPage/', StudentListView.as_view(), name='Student'),
    path('StudentPage/<int:pk>', StudentDetailView.as_view(), name='Student_detail'),
    path('StudentPage/create', StudentCreateView.as_view(), name='Student_create'),
    path('StudentPage/<int:pk>/edit', StudentUpdateView.as_view(), name='Student_update'),
    path('StudentPage/<int:pk>/delete', StudentDeleteView.as_view(), name='Student_delete'),
    path('FacultyPage/', FacultyListView.as_view(), name='Faculty'),
    path('FacultyPage/<int:pk>', FacultyDetailView.as_view(), name='Faculty_detail'),
    path('FacultyPage/create', FacultyCreateView.as_view(), name='Faculty_create'),
    path('FacultyPage/<int:pk>/edit', FacultyUpdateView.as_view(), name='Faculty_update'),
    path('FacultyPage/<int:pk>/delete', FacultyDeleteView.as_view(), name='Faculty_delete'),
    path('SubjectPage/', SubjectListView.as_view(), name='Subject'),
    path('SubjectPage/<int:pk>', SubjectDetailView.as_view(), name='Subject_detail'),
    path('SubjectPage/create', SubjectCreateView.as_view(), name='Subject_create'),
    path('SubjectPage/<int:pk>/edit', SubjectUpdateView.as_view(), name='Subject_update'),
    path('SubjectPage/<int:pk>/delete', SubjectDeleteView.as_view(), name='Subject_delete'),
]