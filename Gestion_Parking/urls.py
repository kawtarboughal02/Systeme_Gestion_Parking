from django.contrib import admin
from django.urls import path
from .views import Accueil,About,ListeClients,Ajouter_Client,Supprimer_Client,ModifierClient
from .views import ListeReservation,Ajouter_Reservation,ModifierReservation,Supprimer_Reservation
from .views import ListePlacesLibres,Ajouter_PlacesLibres,ModifierPlacesLibres
from .views import ListeAbonnement,Ajouter_Abonnement,ModifierAbonnement
urlpatterns = [
    path('', Accueil.as_view(), name='Accueil'),
    path('About', About.as_view(), name='About'),

    path('ListeClients',ListeClients.as_view(),name='ListeClients'),
    path('AjouterClient',Ajouter_Client.as_view(),name='AjouterClient'),
    path('SupprimerClient',Supprimer_Client.as_view(),name='SupprimerClient'),
    path('ModifierClient/<str:code>/', ModifierClient.as_view(), name='ModifierClient'),

    path('ListeReservation',ListeReservation.as_view(),name='ListeReservation'),
    path('AjouterReservation',Ajouter_Reservation.as_view(),name='AjouterReservation'),
    path('SupprimerReservation/<int:id>/',Supprimer_Reservation.as_view(),name='SupprimerReservation'),
    path('ModifierReservation/<int:id>/',ModifierReservation.as_view(),name='ModifierReservation'),

    path('ListePlacesLibres',ListePlacesLibres.as_view(),name='ListePlacesLibres'),
    path('AjouterPlacesLibres',Ajouter_PlacesLibres.as_view(),name='AjouterPlacesLibres'),
    path('ModifierPlacesLibres/<int:id>/', ModifierPlacesLibres.as_view(), name='ModifierPlacesLibres'),

    path('ListeAbonnement', ListeAbonnement.as_view(), name='ListeAbonnement'),
    path('AjouterAbonnement', Ajouter_Abonnement.as_view(), name='AjouterAbonnement'),
    path('ModifierAbonnement/<int:id>/', ModifierAbonnement.as_view(), name='ModifierAbonnement'),



]
