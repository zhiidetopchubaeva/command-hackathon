from django.contrib import admin

from .models import Category, Anime, Comment, Rating, Like, Favoritos

admin.site.register(Category)
admin.site.register(Anime)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Like)
admin.site.register(Favoritos)