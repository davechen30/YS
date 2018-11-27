import logging

from django.db.models import Q
from django.forms import model_to_dict

from mine.apps.component.models import Component


logger = logging.getLogger(__name__)

def getComponentList(componentSet):
    qor = Q()
    if (componentSet.__len__() != 0):
        for componentType in componentSet:
            qor.add(Q(code=componentType), Q.OR)
    list = []
    for i in Component.objects.filter(qor).values(*['code','path']):
        list.append(i)
    return list