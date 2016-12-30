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


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registeration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # create object from form but didn't save it into db yet
            user = form.save(commit=False)

            # clean (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)

            user.save()

            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            # if user is authenticated and is active then redirect to index
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
        # if user is not authenticated then render the form page again
        return render(request, self.template_name, {'form': form})
