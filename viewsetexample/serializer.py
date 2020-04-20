from rest_framework.serializers import ModelSerializer

from viewsetexample.models import University


class UniversitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'address']