from django.conf.urls import url

from music import views

urlpatterns = [
    # music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # music/{id}
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
