from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'  # changes 'object_list' to whatever name you want to render into the template page

    def get_queryset(self):
        return Album.objects.all()  # normally return  as 'object_list' for the rendered page to use


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
