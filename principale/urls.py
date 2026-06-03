from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logements/', views.listings, name='listings'),
    path('logements/<int:listing_id>/', views.listing_detail, name='listing_detail'),
    path('reservation/', views.reservation, name='reservation'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('a-propos/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
