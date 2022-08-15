from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import AnimeViewSet, CategoryViewSet

router = DefaultRouter()
router.register('anime', AnimeViewSet)
router.register('categories', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
   
]


