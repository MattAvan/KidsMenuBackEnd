from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'foods', views.FoodViewSet)
router.register(r'kids', views.KidViewSet)
router.register(r'scores', views.ScoreViewSet)
router.register(r'datemenus', views.DateMenuViewSet)

urlpatterns = [
    path('', include(router.urls))
]