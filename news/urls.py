from django.urls import path
from movie import views  # Importo desde movie

urlpatterns = [
    path('', views.news, name='news')
]
