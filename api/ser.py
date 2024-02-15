from rest_framework import serializers
from . import models

class ListGet(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'