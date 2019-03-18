from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from hello.models import Greeting
from hello.serializers import GreetingSerializer


# Create your views here.
def index(request):
    return render(request, "index.html")


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})


class Greetings(APIView):
    """
    View to list all greetings in the system.
    """

    def get(self, request, format='json'):
        """
        Return a list of all greetings.
        """
        greetings = Greeting.objects.all()
        greeting_serializer = GreetingSerializer(greetings, many=True)
        return Response(greeting_serializer.data, status.HTTP_200_OK)
