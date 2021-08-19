from django.shortcuts import render
from .models import HomeModel, AboutModel

# Create your views here.


def home(request):
    homedata = HomeModel.objects.all()

    context = {'homedata': homedata}
    return render(request, 'portfolio/home.html', context)


def about(request):
    aboutdata = AboutModel.objects.all()

    context = {'aboutdata': aboutdata}
    return render(request, 'portfolio/about.html', context)
