from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('logements/', views.logements, name='logements'),
    path('logements/ajouter/', views.logement_form, name='logement_ajouter'),
    path('logements/<int:pk>/modifier/', views.logement_form, name='logement_modifier'),
    path('logements/<int:pk>/supprimer/', views.logement_supprimer, name='logement_supprimer'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations/<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('reservations/<int:pk>/confirmer/', views.reservation_confirmer, name='reservation_confirmer'),
    path('reservations/<int:pk>/annuler/', views.reservation_annuler, name='reservation_annuler'),
    path('reservations/<int:pk>/supprimer/', views.reservation_supprimer, name='reservation_supprimer'),
    path('parametres/', views.parametres, name='parametres'),
]
