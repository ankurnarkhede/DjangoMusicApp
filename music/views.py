

from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from .forms import UserForm
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from .models import Album, Song
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):
    model = Album
    template_name ='music/detail.html'


@method_decorator(login_required, name='dispatch')
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


@method_decorator(login_required, name='dispatch')
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


@method_decorator(login_required, name='dispatch')
class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


    
# song crud
@method_decorator(login_required, name='dispatch')
class SongCreate(CreateView):
    model = Song
    fields = ['album', 'audio_file', 'song_title', 'is_favorite']


@method_decorator(login_required, name='dispatch')
class SongUpdate(UpdateView):
    model = Song
    fields = ['album', 'audio_file', 'song_title', 'is_favorite']


@method_decorator(login_required, name='dispatch')
class SongDelete(DeleteView):
    model = Song

    def get_success_url(self):
        album = self.object.album
        return reverse_lazy ('music:detail', kwargs={'pk': album.id})


    

class UserFormView(View):
    form_class=UserForm
    template_name='music/registration_form.html'

    # display blank form
    def get(self, request):
        if request.user.is_authenticated ():
            return HttpResponseRedirect (reverse ('music:index'))
        form=self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        if request.user.is_authenticated ():
            return HttpResponseRedirect(reverse ('music:index'))
        form=self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)

            # cleaned normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            user=authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render (request, self.template_name, {'form': form})


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated ():
            return HttpResponseRedirect(reverse ('music:index'))
        return render (request, "music/login.html")

    def post(self, request):
        if request.user.is_authenticated ():
            return HttpResponseRedirect(reverse ('music:index'))
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse ('music:index'))
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect (reverse ('music:login_user'))


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        form = UserForm (request.POST or None)
        # context = {
        #     "form": form,
        # }
        return HttpResponseRedirect (reverse ('music:login_user'))










# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 albums = Album.objects.filter(user=request.user)
#                 return render(request, 'music/index.html', {'albums': albums})
#             else:
#                 return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
#         else:
#             return render(request, 'music/login.html', {'error_message': 'Invalid login'})
#     return render(request, 'music/login.html')



# def register(request):
#     form = UserForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user.set_password(password)
#         user.save()
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 albums = Album.objects.filter(user=request.user)
#                 return render(request, 'music/index.html', {'albums': albums})
#     context = {
#         "form": form,
#     }
#     return render(request, 'music/register.html', context)
#
#











# from django.shortcuts import render, get_object_or_404
# from .models import Album, Song

# def index(request):
#     all_albums=Album.objects.all()
#     context={
#         'all_albums':all_albums,
#     }
#     return render(request,'music/index.html', context)
#
#
# def detail(request, album_id):
#     album=get_object_or_404(Album, pk=album_id)
#
#     # try:
#     #     album=Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does not exists")
#
#     return render(request, 'music/detail.html',{'album':album})
#
# def favorite(request, album_id):
#     album=get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song=album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#             'album':album,
#             'error_message':'You did not select a valid song',
#         })
#     else:
#         selected_song.is_favorite=True
#         selected_song.save()
#         return render (request, 'music/detail.html', {'album': album})







