from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = 'school/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "rahim"
        context['rno'] = 101
        return context
    
class ExtracContextTemplateView(TemplateView):
    template_name = 'school/h1.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "rahim"
        context['rno'] = 101
        context = {"name":"Rahim","caste":"Wazir"}    #if i write context on this mannner instead of the above then i will be not able to get extra context and url
        print(kwargs)
        return context