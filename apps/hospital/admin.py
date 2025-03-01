from django.contrib import admin
from .models import Region, Hospital, ImageHospital, Department, Doctor

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region', 'phone', 'created_date')
    search_fields = ('name', 'region__name')
    list_filter = ('region',)
    readonly_fields = ('created_date', 'updated_date')

@admin.register(ImageHospital)
class ImageHospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'hospital', 'image')
    search_fields = ('hospital__name',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'hospital', 'name')
    search_fields = ('hospital__name', 'name')
    list_filter = ('hospital',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hospital', 'department', 'specialty', 'phone')
    search_fields = ('name', 'specialty', 'hospital__name', 'department__name')
    list_filter = ('hospital', 'department')
