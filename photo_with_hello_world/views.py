from django.shortcuts import render
from photo_with_hello_world.models import Photo
from .utils import change_photo


def photoPageView(request):

    if request.method == 'GET':
        photo = Photo.objects.all()
        change_photo(photo)

        objects_list = {'object_list':photo}
        return render(request, 'main.html', objects_list)
