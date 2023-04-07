from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
import django_filters
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
import requests, os
from dotenv import load_dotenv

# Create your views here.
load_dotenv()

TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')
 

class CompanyViewSet(ViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    lookup_field = 'name'

    def get_object(self, name):
        try:
            obj = Company.objects.get(name=name)
            self.check_object_permissions(self.request, obj)
            return obj
        except Company.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """The method for creating new instances of Company Model"""
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        """The method for listing all the companies."""
        query = request.GET.get('query')
        if not query:
            query = ''
        companies = Company.objects.filter(Q(name__icontains=query) | Q(slogan__icontains=query))
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        """The method for retrieving a specific company"""
        name = self.kwargs['name']
        company = self.get_object(name=name.title())
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, name):
        """The method for updating an existing Company instance"""
        company = self.get_object(name=name)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, name):
        """The method for deleting a particular Company instance"""
        self.get_object(name).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class AdvocateViewSet(ViewSet):
    serializer_class = AdvocateSerializer
    # permission_classes = [IsAuthenticated]
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
        username = self.kwargs['username']
        advocate = self.get_object(username=username.title())
        serializer = AdvocateSerializer(advocate)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, username):
        """The method for updating an existing Advocate instance"""
        instance = self.get_object(username)
        serializer = AdvocateSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, username):
        """The method for deleting a particular Advocate instance"""
        instance = self.get_object(username)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)