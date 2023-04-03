from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Advocate
from .serializers import AdvocateSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return JsonResponse(data, safe=False)

class AdvocateViewSet(ViewSet):

    def create(self, request):
        """The method for creating new instances of Advocate Model"""
        serializer = AdvocateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        """The method for listing all the advocates."""
        advocates = Advocate.objects.all()
        serializer =AdvocateSerializer(advocates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)