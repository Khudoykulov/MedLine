from django.urls import path
from .views import (
    RegionListView,
    HospitalListView, HospitalDetailView,
    DepartmentListView, DepartmentDetailView,
    DoctorListView, DoctorDetailView
)

app_name = 'hospital'

urlpatterns = [
    # **Region URLs**
    path('', HospitalListView.as_view(), name='region-list'),

    # **Hospital URLs**
    # path('hospitals/', HospitalListView.as_view(), name='hospital-list'),
    # path('hospitals/<int:pk>/', HospitalDetailView.as_view(), name='hospital-detail'),
    #
    # # **Department URLs**
    # path('departments/', DepartmentListView.as_view(), name='department-list'),
    # path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    #
    # # **Doctor URLs**
    # path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    # path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
]
