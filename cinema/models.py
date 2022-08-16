from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Anime(models.Model):
    categories = models.ManyToManyField(Category, related_name='anime')
    name = models.CharField(max_length=50)
    opisanie = models.TextField()
    seria = models.IntegerField()
    year = models.DateField()
    image = models.ImageField(
        upload_to="media")

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        ratings = [rating.value for rating in self.ratings.all()]
        if ratings:
            return sum(ratings) / len(ratings)
        return 0

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])

    def __str__(self):
        return f'{self.user}: {self.anime}. Rating: {self.value}'


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body



class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f'LIKE TO ANIME: {self.anime}  FROM USER: {self.user}'

