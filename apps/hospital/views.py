from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Region, Hospital, Department, Doctor
from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView


class Home(TemplateView):
    template_name = 'index.html'


# **1. Region Views**
# class RegionListView(TemplateView):
#     template_name = 'navbar.html'
#
#     def get_context_data(self,  **kwargs):
#         cnt = super().get_context_data(**kwargs)
#         cnt['regions'] = Region.objects.order_by('id')
#         print("Regions:", cnt['regions'])
#         print('asassasaa')# Konsolga chiqarib ko‘rish
#         return cnt


# **2. Hospital Views**
class HospitalListView(View):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        region_name = request.GET.get('region')

        if region_name:
            hospitals = Hospital.objects.filter(region__name=region_name)  # Faqat tanlangan regionni olish
        else:
            hospitals = Hospital.objects.all()

        ctx = {
            'hospitals': hospitals,
        }
        return render(request, 'blog.html', ctx)


class HospitalDetailView(DetailView):
    model = Hospital
    template_name = 'blog.html'
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
