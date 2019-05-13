from django.shortcuts import render
from .models import Photo

def home(request):
    context={
        'photos':Photo.objects.all()
    }
    return render(request, 'photos/home.html',context)

def photo(request, photo_id):
    photo = Photo.objects.get(id = photo_id)
    return render(request, 'photos/photos.html', {"photo":photo})