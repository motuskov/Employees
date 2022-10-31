from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.http import Http404
from .models import *

class MainView(TemplateView):
    '''
    The MainView object forms content for index.html page.
    '''
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['departments'] = Department.objects.all()

        return context

class EmployeeListView(ListView):
    '''
    The EmployeeListView objects renders employee lists of departments.

    Attributes:
        department(models.Department): department for which the list of
    employees is requested
    '''
    template_name = 'mainapp/ajax/employee_list.html'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        # Look for requesting Department object
        try:
            department_pk = int(request.GET.get('department'))
        except ValueError:
            raise Http404('Primary key format error')
        self.department = get_object_or_404(
            Department,
            pk=department_pk
        )

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # Get employees of requested department and all descendants
        departments = self.department.get_descendants(include_self=True)
        employees = Employee.objects.filter(department__in=departments)

        return employees

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['department'] = self.department

        return context
