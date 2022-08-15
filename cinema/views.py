from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Anime, Comment, Like 
from .serializer import CommentSerializer
from .permissions import IsAuthor

class CommentViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

@api_view(["GET"])
def toggle_like(request, p_id):
    user = request.user
    product = get_object_or_404(Anime, id=p_id)

    if Like.objects.filter(user=user, product=product).exists():
        Like.objects.filter(user=user, product=product).delete()
    else:
        Like.objects.create(user=user, product=product)
    return Response("Like toggled", 200)

@api_view(["POST"])
def add_rating(request, p_id):
    user = request.user
    product = get_object_or_404(Anime, id=p_id)
    value = request.POST.get("value")

    if not user.is_authenticated:
        raise ValueError("authentication credentials are not provided")

    if not value:
        raise ValueError("value is required")
    
    if rating.objects.filter(user=user, product=product).exists():
        rating = rating.objects.get(user=user, product=product)
        rating.value = value
        rating.save()
    else:
        rating.objects.create(user=user, product=product, value=value)
    
    return Response("rating created", 201)
