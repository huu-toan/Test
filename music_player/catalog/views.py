from django.shortcuts import render
from catalog.models import Song
from django.db.models import Count
from django.db.models import F
from django.shortcuts import get_object_or_404

def index(request):
    song = Song.objects.all()
    return render(request, 'homepage/song_card.html', {'song': song})

def songs(request):
    song = Song.objects.all()
    # dd(song)
    return render(request, 'song_page/song_page.html', {'song': song})
# {'song': song}: can co cai nay, o day de tra bien song ve 'song_page/song_page.html' duoi dang object ten la 'song'. Cai o trong '' la ten bien ma o muon tra n ve, cai sau dau : la bien o muon tra ve

def songpost(request, id):
    song = Song.objects.get(pk = id)
    song.listen_count = F('listen_count') + 1
    song.save()
    return render(request, 'song_page/songpost.html', {'song': song})


def search(request):
    query = request.GET.get("query")
    qs = Song.objects.filter(name__icontains=query)
    return render(request, 'song_page/search.html', {"songs": qs})

def mostdownloaded(request):
    song = Song.objects.all().order_by('-listen_count')
    return render(request, 'song_page/mostdownloaded.html', {'mostdownloaded': mostdownloaded})

def trending(request):
    trending = Song.objects.all().order_by('-listen_count')
    return render(request, 'song_page/trending.html', {'trending': trending})
