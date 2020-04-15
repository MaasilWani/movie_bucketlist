from django.contrib import admin
from movieApp.models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Actor', 'Actress', 'Date', 'Rating']

admin.site.register(Movie, MovieAdmin)