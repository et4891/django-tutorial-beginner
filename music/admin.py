from django.contrib import admin
from .models import Album, Song

#  # Register Album, Song class into admin page
admin.site.register(Album)  # Register Album class into admin page
admin.site.register(Song)
