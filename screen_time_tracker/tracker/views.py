from django.shortcuts import render
from rest_framework import generics, status
from .models import category
from .serializers import categorySerializer, hoursSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import helper.data_visualization as data_visualization
# Create your views here.

class categoryView(generics.ListAPIView):
    queryset = category.objects.all()
    serializer_class = categorySerializer

class hoursView(APIView):
    serializer_class = hoursSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        res = {}
        h = request.data['hours']
        cat = data_visualization.utilities.last_hours_category("01:02:22", h+1)

        for i in range(len(cat)):
            print(cat[i].name, cat[i].time)
            res[cat[i].name] = cat[i].time
            
        return Response(res, status=status.HTTP_201_CREATED)

class usageView(APIView):
    def post(self, request, format=None):
        res = {}
        h = request.data['usage']
        if(h=="today"):
            pass
            
        return Response({h}, status=status.HTTP_201_CREATED)
        