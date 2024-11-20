from django.shortcuts import render
from gallery.models import Gallery
from portfolio.models import Portfolio
from reviews.models import Reviews
from courses.models import Courses


def home_view(request):
    data = {}
    gallery = Gallery.objects.filter(is_archived = False)
    data['gallery'] = gallery
    portfolio = Portfolio.objects.filter(is_archived = False)
    data['portfolio'] = portfolio
    reviews = Reviews.objects.filter(is_archived = False)
    data['reviews'] = reviews
    courses = Courses.objects.filter(is_archived = False)
    data['courses'] = courses
    return render(request, 'index.html', context= data)