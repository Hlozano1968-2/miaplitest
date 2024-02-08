from django.urls import path,include
from rest_framework import routers
from .views import ProductoViewSet

ruta = routers.DefaultRouter()
ruta.register('producto',ProductoViewSet)

urlpatterns = [
    path('', include(ruta.urls)),
]