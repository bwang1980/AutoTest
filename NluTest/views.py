from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TestCase
# Create your views here.
def index(request):
    caseList = TestCase.objects.all()
    template = loader.get_template('NluTest/index.html')
    context = {
        'cases':caseList,
    }
    return HttpResponse(template.render(context, request))