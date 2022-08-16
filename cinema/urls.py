from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import AnimeViewSet, CategoryViewSet, CommentViewSet, toggle_like, add_rating, add_to_favoritos, FavoritosViewSet

router = DefaultRouter()
router.register('anime', AnimeViewSet)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)
router.register('favoritos', FavoritosViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('anime/toggle_like/<int:a_id>/', toggle_like),
    path('anime/add_rating/<int:a_id>/', add_rating),
    path('anime/add_to_favoritos/<int:a_id>/', add_to_favoritos),
   
]


