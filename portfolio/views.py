from django.shortcuts import render
from .models import HomeModel

# Create your views here.


def home(request):
    homedata = HomeModel.objects.all()

    context = {'homedata': homedata}
    return render(request, 'portfolio/home.html', context)


def about(request):
    return render(request, 'portfolio/about.html')
