from django.views import generic
from .models import Album


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'  # changes 'object_list' to whatever name you want to render into the template page

    def get_queryset(self):
        return Album.objects.all()  # normally return  as 'object_list' for the rendered page to use


class DetailView(generic.DeleteView):
    model = Album
    template_name = 'music/detail.html'
