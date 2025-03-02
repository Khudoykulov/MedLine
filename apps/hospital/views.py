from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Region, Hospital, Department, Doctor
from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView


# **1. Region Views**
class RegionListView(TemplateView):
    template_name = 'navbar.html'

    def get_context_data(self,  **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt['regions'] = Region.objects.order_by('id')
        print("Regions:", cnt['regions'])
        print('asassasaa')# Konsolga chiqarib ko‘rish
        return cnt



# **2. Hospital Views**
class HospitalListView(ListView):
    model = Hospital
    template_name = 'blog.html'
    context_object_name = 'hospitals'


class HospitalDetailView(DetailView):
    model = Hospital
    template_name = 'index.html'
    context_object_name = 'hospital'


# **3. Department Views**
class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department_detail.html'
    context_object_name = 'department'


# **4. Doctor Views**
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor_list.html'
    context_object_name = 'doctors'


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor_detail.html'
    context_object_name = 'doctor'
