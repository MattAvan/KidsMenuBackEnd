from rest_framework import viewsets, filters
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Food, Kid, Score, DateMenu
from .serializers import FoodSerializer, KidSerializer, ScoreSerializer, DateMenuSerializer
from rest_framework import permissions

class FoodViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['foodName']

class KidViewSet(viewsets.ModelViewSet):
    queryset = Kid.objects.all()
    serializer_class = KidSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class DateMenuViewSet(viewsets.ModelViewSet):
    queryset = DateMenu.objects.all()
    serializer_class = DateMenuSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {'date': ['exact', 'lte', 'gte'], 'mealTime': ['exact']}