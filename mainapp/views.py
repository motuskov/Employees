from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View
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

class EmployeeListView(View):
    '''
    The EmployeeListView objects renders employee lists of departments.
    '''
    def get(self, request, *args, **kwargs):
        # Look for requesting Department object
        try:
            department_pk = int(request.GET.get('department'))
        except ValueError:
            raise Http404('Primary key format error')
        department = get_object_or_404(
            Department,
            pk=department_pk
        )

        # Create context for rendering employee list
        context = {
            'employees': department.employees.all()
        }

        return render(request, 'mainapp/ajax/employee_list.html', context)
