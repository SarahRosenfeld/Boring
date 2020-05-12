from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# home page for suggestions
def home_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'suggestions/home.html', context)

def about_page(request):
    return render(request, 'suggestions/about.html')
