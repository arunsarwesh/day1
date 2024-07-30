from django.shortcuts import render
from . import models

def books(request):
    books = models.Books.objects.all().values()
    cont ={
        "books":books
    }
    return render(request, 'index.html',cont)
# Create your views here.
