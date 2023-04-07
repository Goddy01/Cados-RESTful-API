from .models import Advocate, Company
from rest_framework.serializers import ModelSerializer

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocate
        fields = '__all__'