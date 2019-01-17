from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from material.models import rawMaterials


def home(request):
    rawmaterial = rawMaterials.objects.get(name='TS')
    return render(request, 'home.html', {'rawmaterial': rawmaterial})

