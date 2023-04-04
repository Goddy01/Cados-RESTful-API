from .models import Advocate
from rest_framework.serializers import ModelSerializer

class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = ['username', 'bio']