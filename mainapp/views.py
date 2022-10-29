from django.shortcuts import render
from django.views.generic import TemplateView

class MainView(TemplateView):
    '''
    The MainView object forms content for index.html page.
    '''
    template_name = 'mainapp/index.html'
