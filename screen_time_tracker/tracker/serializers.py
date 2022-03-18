from rest_framework import serializers
from .models import category

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ('name', 'hours', 'minutes', 'seconds', 'time')

class hoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ('hours') # should change this to start hour