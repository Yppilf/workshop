from django.urls import path
from . import views

urlpatterns = [
    path('', views.star_list, name='star_list'),
    path('telescopes', views.telescope_list, name='telescope_list'),
    path('add_star/', views.add_star, name='add_star'),
]