from .models import Advocate
from rest_framework.serializers import ModelSerializer

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = ['name', 'slogan']

class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = ['username', 'bio']