from django.http import HttpResponse
import json
import MySQLdb
from django.shortcuts import render
from django.core import serializers
# Create your views here.
from django.utils.safestring import mark_safe

from material.models import rawMaterials, RedMud, HeavySetalSlag


def sectorgraph(request, rawmaterial_id):
    rawmaterial = rawMaterials.objects.get(pk=rawmaterial_id)
    return render(request, 'sectorGraph.html', {'rawmaterial': rawmaterial})


def linegraph(request):
    rate_list = list(HeavySetalSlag.objects.values_list('rate', flat=True))
    temp_list = list(HeavySetalSlag.objects.values_list('temp', flat=True))
    t_list = []
    for i in range(len(temp_list)):
        a = str(temp_list[i])
        t_list.append(a)
    t_list = mark_safe(t_list)
    return render(request, 'lineGraph.html', {'temp': t_list, 'rate': rate_list})
