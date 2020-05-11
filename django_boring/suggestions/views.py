from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Sarah',
        'title': 'Community',
        'content': 'TV Show',
        'service': 'Netflix'
    },
    {
        'author': 'Ian',
        'title': 'Jerry McGuire',
        'content': 'Movie',
        'service': 'Netflix'
    }
]
# home page for suggestions
def home_page(request):
    context = {
        'posts': posts
    }
    return render(request, 'suggestions/home.html', context)

def about_page(request):
    return render(request, 'suggestions/about.html')
