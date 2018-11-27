from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Organization
#         fields = ('name','create_time','change_user_name','change_time','remark')
#
# class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Department
#         fields = ('name','organization','create_time','change_user_name','change_time','remark')
#
# class PositionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Position
#         fields = '__all__'
#
# class RoelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Roel
#         fields = '__all__'

#
# class TokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Roel
#         fields = '__all__'