from django.shortcuts import render
from .models import Photo

def welcome(request):
    return render(request, 'photos/welcome.html', {'title': 'welcome'})

def main(request):
    context={
        'photos':Photo.objects.all()
    }
    return render(request, 'photos/home.html',context)

def photo(request, photo_id):
    photo = Photo.objects.get(id = photo_id)
    return render(request, 'photos/photos.html', {"photo":photo})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_articles = Photo.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"photos": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})