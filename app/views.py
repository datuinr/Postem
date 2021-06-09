from django.shortcuts import get_object_or_404, render
from .models import Category, Poster


def categories(request):
    return {
        'categories': Category.objects.all()
    }

def index(request):
    posters = Poster.objects.all()
    return render(request, 'index.html', {'posters': posters})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def poster_detail(request, slug):
    poster = get_object_or_404(Poster, slug=slug, in_stock=True)
    return render(request, 'detail.html', {'poster': poster})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posters = Poster.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'posters': posters})