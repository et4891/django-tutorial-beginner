from django.http import Http404
from django.shortcuts import render
from .models import Album


# Create your views here.
def index(request):
    title = 'Albums'
    all_albums = Album.objects.all()  # connect to db and get all Album's rows
    return render(request, 'music/index.html', {'all_albums': all_albums, 'title': title})


def detail(request, album_id):
    # return HttpResponse('album number ' + str(album_id))
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404('Album does not exist')
    return render(request, 'music/detail.html', {'album': album})
