from django.db import models
from django.contrib.auth.models import User


class Clients(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    Nom = models.CharField(max_length=50, null=True, blank=True)
    Prenom = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    Password = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.Nom

class PlacesLibres(models.Model):

    NombrePlaceDisponible = models.IntegerField(null=True, blank=True, default=0)
    NombrePlaceReserver = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f"Places libres : {self.NombrePlaceDisponible}"

class Reservations (models.Model):

    idReservation = models.IntegerField(null=True, blank=True, default=0)
    dateDebut = models.DateField(null=True)
    dateFin = models.DateField(null=True)
    Prix = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    code = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"Reservation {self.idReservation}"

class Abonnements(models.Model):
    TypeAbonnement = models.CharField(max_length=200, null=True, blank=True)
    DureeAbonnement= models.CharField(max_length=200, null=True, blank=True)
    Prix = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.TypeAbonnement