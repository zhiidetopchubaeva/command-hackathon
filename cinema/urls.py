from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import AnimeViewSet, CategoryViewSet, CommentViewSet, toggle_like, add_rating

router = DefaultRouter()
router.register('anime', AnimeViewSet)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('anime/toggle_like/<int:a_id>/', toggle_like),
    path('anime/add_rating/<int:a_id>/', add_rating),
   
]


