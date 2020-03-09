from django.shortcuts import render

# Create your views here.
from store.models import Book


def index(request):
    return render(request, 'template.html')


def store(request):
    count = Book.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, 'store.html', context)
