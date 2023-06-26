from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Hello


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "pk", "name"


class HelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hello
        fields = "message",

