from rest_framework import serializers


from .models import Anime, Category, Comment, Like, Rating

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        rep['ratings'] = instance.average_rating
        rep['likes'] = instance.likes.all().count()
        rep['liked_by_user'] = False
        rep['user_rating'] = 0

        request = self.context.get('request')
        if request.user.is_authenticated:
            rep['liked_by_user'] = Like.objects.filter(user=request.user, anime=instance).exists()
            if Rating.objects.filter(user=request.user,anime=instance).exists():
                rating = Rating.objects.get(user=request.user,anime=instance)
                rep['user_rating'] = rating.value

        return rep

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

