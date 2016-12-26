from django.db import models
from django.core.urlresolvers import reverse


# Example on creating an Album object
# album1 = Album(artist='Lady Gaga', album_title='Paparazzi', genre='Pop', album_logo='https://upload.wikimedia.org/wikipedia/en/f/f1/Paparazzi_cover.png')
# album1.save()
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.artist + '-' + self.album_title + ' (id-' + str(self.id) + ')'


# Example on creating an Song object using the album object example above
# b.song_set.create(file_type='mp3', song_title='I love bacon')
# the above would auto save
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  # songs will be deleted if album is deleted
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title + ' (id-' + str(self.id) + ')'
