from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm
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


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('index')