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
    rate_list = list(HeavySetalSlag.objects.values_list('rate', flat=True))
    temp_list = list(HeavySetalSlag.objects.values_list('temp', flat=True))
    t_list = []
    for i in range(len(temp_list)):
        a = str(temp_list[i])
        t_list.append(a)
    t_list = mark_safe(t_list)
    name = mark_safe('含重金属渣')

    return render(request, 'sectorGraph.html', {'rawmaterial': rawmaterial,'name': name, 'temp': t_list, 'rate': rate_list})


def linegraph(request):

    rate_list = list(HeavySetalSlag.objects.values_list('rate', flat=True))
    temp_list = list(HeavySetalSlag.objects.values_list('temp', flat=True))
    t_list = []
    for i in range(len(temp_list)):
        a = str(temp_list[i])
        t_list.append(a)
    t_list = mark_safe(t_list)
    name = mark_safe('含重金属渣')
    return render(request, 'lineGraph.html', {'name': name, 'temp': t_list, 'rate': rate_list})
