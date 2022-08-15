from itertools import product
from rest_framework import serializers

from .models import Anime, Comment, Like 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'
    
    def to_representation(self, instance:Anime ):
        rep = super().to_representation(instance)
        rep["comments"] = CommentSerializer(instance.comments.all(), many=True).data
        rep["likes"] = instance.likes.all().count()
        rep["rating"] = instance.get_average_rating()
        rep["liked_by_user"] = False
        rep["user_rating"] = 0

        request = self.context.get("request")

        if request.user.is_authenticated:
            rep["liked_by_user"] = Like.objects.filter(user=request.user, product=instance).exists()
            if rating.objects.filter(user=request.user, product=instance).exists():
                rating = rating.objects.get(user=request.user, product=instance)
                rep["user_rating"] = rating.value

        return rep


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['user']

    def create(self, validated_data):
        validated_data["user"] = self.context.get("request").user
        return super().create(validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["user"] = instance.user.email
        return rep

