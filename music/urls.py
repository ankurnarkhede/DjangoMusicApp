from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

app_name='music'


urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index' ),

    url (r'^register/$', views.UserFormView.as_view (), name='register'),

    url (r'^logout/$', views.LogoutView.as_view(), name='logout'),

    url (r'^login/$', views.LoginView.as_view(), name='login_user' ),
    # url (r'^login/$', views.LoginView.as_view(redirect_authenticated_user=True), name='login_user' ),


    # music urls
    # /music/<album.id>...for album id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2
    url (r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view (), name='album-update'),

    # /music/album/2/delete
    url (r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view (), name='album-delete'),


    # song urls
    # /music/song/add
    url (r'^song/add/$', views.SongCreate.as_view (), name='song-add'),

    # /music/album/2
    url (r'^song/(?P<pk>[0-9]+)/$', views.SongUpdate.as_view (), name='song-update'),

    # /music/album/2/delete
    url (r'^song/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view (), name='song-delete'),




    # /music/<album.id>/favorite
    # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),


]






