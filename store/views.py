from django.shortcuts import redirect, render ,get_object_or_404
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"store/index.html")

def genres(request):
    genre = Genre.objects.filter(status=0)
    context = {'genre': genre}
    return render(request,"store/genres.html",context)

def genresview(request, genre):
    genre_obj = Genre.objects.get(name = genre)
    products = Product.objects.filter(genre = genre_obj)
    genre_name = Genre.objects.filter(name=genre_obj.name).first()
    if not products:
        messages.warning(request, "No books found in this genre.")
    context = {'products': products,'genre_name':genre_name}
    return render(request,"store/products/index.html",context)


def productview(request, genre_name, prod_id):
    genre = get_object_or_404(Genre, name=genre_name, status=0)
    product = get_object_or_404(Product, id=prod_id, status=0)
    context = {'product': product}
    return render(request, "store/products/view.html", context)
