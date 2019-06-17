from django.contrib import admin
from mdb.models import Movie, MovieRate, MovieActor, MovieDirector

admin.site.register(Movie)
admin.site.register(MovieRate)
admin.site.register(MovieActor)
admin.site.register(MovieDirector)