from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.
# NavPower ButtonPower NavItem
class NavItemViewSet(viewsets.ModelViewSet):
    queryset = NavItem.objects.all()
    serializer_class = NavItemSerializer


class ButtonPowerViewSet(viewsets.ModelViewSet):
    queryset = ButtonPower.objects.all()
    serializer_class = ButtonPowerSerializer


class NavPowerViewSet(viewsets.ModelViewSet):
    queryset = NavPower.objects.all()
    serializer_class = NavPowerSerializer