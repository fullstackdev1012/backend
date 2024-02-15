from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models, ser

@api_view(['GET'])
def getData(request):
    items = models.Item.objects.all()
    serli = ser.ListGet(items, many=True)
    return Response(serli.data)


