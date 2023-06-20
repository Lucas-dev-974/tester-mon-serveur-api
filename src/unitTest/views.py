from django.shortcuts import render
from unitTest.models import Game
from rest_framework import viewsets
from unitTest.serializers import GameSerializer


# Create your views here.
# def home(request):
#     return render(request, "home.html", {})

class GameViewset(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
