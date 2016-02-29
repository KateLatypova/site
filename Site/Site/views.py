from django.shortcuts import render

from gallery.models import AlbumImage


def index_page(request):
    return render(request, 'index.html', {})

def description_page(request):
    return render(request, 'description.html', {})

def gallery_page(request):
    args = {}
    img_list = AlbumImage.objects.all()
    args['images'] = img_list
    return render(request, 'gallery.html', args)

def visit_page(request):
    return render(request, 'visit.html', {})
