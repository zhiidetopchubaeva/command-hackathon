
from django.http import QueryDict
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins, filters
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response


from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Anime, Category
from .serializers import AnimeSerializer, CategorySerializer



class AnimeViewSet(ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'year']


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('name', openapi.IN_QUERY, 'search products by name', type=openapi.TYPE_STRING)])


    @action(methods=['GET'], detail=False)
    def search(self, request):
        name = request.query_params.get('name')
        queryset = self.get_queryset()
        if name:
            queryset = queryset.filter(name__icontains=name)
        
        serializer = AnimeSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data, 200)


    @action(methods=['GET'], detail=False)
    def order_by_rating(self, request):
        queryset = self.paginate_queryset()
        queryset = sorted(queryset, key=lambda anime: anime.average_rating, reverse=True)
        serializer = AnimeSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, 200)



class CategoryViewSet(mixins.CreateModelMixin, 
                    mixins.DestroyModelMixin, 
                    mixins.ListModelMixin, 
                    GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

