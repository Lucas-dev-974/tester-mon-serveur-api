from django.urls import path, include
from rest_framework.routers import DefaultRouter
from unitTest.views import GameViewset
from . import views

router = DefaultRouter()
router.register('game', GameViewset, basename='game')

urlpatterns = [
    # path("", views.home, name="home"),
    path('', include(router.urls)),
]
