from django.shortcuts import render
from gallery.models import Category,Location, Image
# Create your views here.
def displayhome(request):
    images = Image.objects.all()
    location=Location.get_locations()
    return render(request, 'home.html',{"images":images,"location":location})


def image_location(request,location_name):
    location=Location.get_locations()
    image= Image.fetch_by_location(location_name)
    message = f"{location_name}"
    return render(request, 'imageLocation.html',{"message":message,"image": image,"location":location})


def image_properties(request,image_id):
    location=Location.get_locations()

    image = Image.get_image_by_id(image_id)
    return render(request, {"image" : image,"location":location})


def search_category(request):

    location=Location.get_locations()

    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        search = Image.search_category(category)
        message = f"{category}"
        return render(request, 'search.html',{"message":message,"category": search,"location":location})
    else:
        return render(request, 'search.html')