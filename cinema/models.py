from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=100)


class Anime(models.Model):
    name = models.CharField(max_length=50)
    opisanie = models.TextField()
    seria = models.IntegerField()
    year = models.DateTimeField()
    image = models.ImageField(
        upload_to="media/films")


class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, related_name='likes', on_delete=models.CASCADE)

class Otzyv(models.Model):
    user = models.ForeignKey(User, related_name='otzyv', on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, related_name='otzyv', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(choices=[(5,5), (6,6), (7,7), (8,8), (9,9), (10,10)])
