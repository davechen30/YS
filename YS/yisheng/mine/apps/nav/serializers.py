from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

# NavPower ButtonPower NavItem
class NavItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NavItem
        fields = '__all__'

class NavPowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NavPower
        fields = '__all__'

class ButtonPowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ButtonPower
        fields = '__all__'

