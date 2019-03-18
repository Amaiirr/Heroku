from rest_framework import serializers
from hello.models import Greeting


class GreetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Greeting
        fields = '__all__'
