from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Person

class PersonSerializer(ModelSerializer):
    user_id = IntegerField()

    class Meta:
        model = Person
        fields = ['user_id', 'bio', 'created_at', 'updated_at',]