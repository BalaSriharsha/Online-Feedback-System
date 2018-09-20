from django.urls import path

from .views import feedback, home

urlpatterns = [
    path('<int:id>/feedback/',
         feedback, name='feedback'),
    path('', home, name='home'),
]
