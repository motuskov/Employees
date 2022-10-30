from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *

@admin.register(EmployeePosition)
class EmployeePositionAdmin(admin.ModelAdmin):
    '''
    The EmployeePositionAdmin object represents a position of an
    employee in the administration interface.
    '''
    list_display = (
        'title',
    )

@admin.register(Department)
class DepartmentAdmin(MPTTModelAdmin):
    '''
    The DepartmentAdmin object represents a department of a compony
    in administration interface.
    '''
    mptt_level_indent = 20

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    '''
    The EmployeeAdmin represents en employee of a company in
    administration interface.
    '''
    list_display = (
        'last_name',
        'first_name',
        'middle_name',
        'department',
        'position',
    )
