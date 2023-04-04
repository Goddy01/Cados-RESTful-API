from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Advocate
from .serializers import AdvocateSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
import django_filters
from rest_framework import filters

# Create your views here.



class AdvocateViewSet(ViewSet):
    serializer_class = AdvocateSerializer
    queryset = Advocate.objects.all()
    lookup_field = 'username'

    def get_object(self, username):
        try:
            obj = Advocate.objects.get(username=username)
            self.check_object_permissions(self.request, obj)
            return obj
        except Advocate.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        """The method for creating new instances of Advocate Model"""
        serializer = AdvocateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        """The method for listing all the advocates."""
        query = request.GET.get('query') # retrieves the search value from request
        if query == None:
            query = ''
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query)) # retrieves Advocate Model instances whose username or bio contains the provided query value
        # advocates = Advocate.objects.all()
        serializer =AdvocateSerializer(advocates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        """The method for retrieving a specific advocate"""
        queryset = Advocate.objects.all()
        username = self.kwargs['username']
        advocate = get_object_or_404(queryset, username=username)
        serializer = AdvocateSerializer(advocate)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, username):
        instance = self.get_object(username)
        serializer = AdvocateSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)