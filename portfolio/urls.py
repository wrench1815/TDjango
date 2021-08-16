from django.urls import path
from portfolio.views import home, about

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
]
