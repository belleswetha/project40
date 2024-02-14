from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse
# Create your views here

class templatehtml(TemplateView):
    template_name='templatehtml.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Sweety'
        ECDO['age']='21'
        return ECDO
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
           SFDO.save()
           return HttpResponse('InsertSchoolByTv is done')
    
    
class InsertSchoolByTv(TemplateView):
    template_name='InsertSchoolByTv.html'
    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('InsertSchoolByFv is done')
