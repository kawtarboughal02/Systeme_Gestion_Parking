from django import forms
from .models import Clients
from .models import Reservations
from .models import PlacesLibres
from .models import Abonnements
from django.forms import widgets

class AjouterClientForm(forms.ModelForm):
    class Meta:
         model = Clients
         fields = ("code","Nom","Prenom","email","username","Password")
         widgets = {
             'code':forms.TextInput(attrs={'class':'form-control'}),
             'Nom':forms.TextInput(attrs={'class':'form-control'}),
             'Prenom':forms.TextInput(attrs={'class':'form-control'}),
             'email':forms.EmailInput(attrs={'class':'form-control'}),
             'username':forms.TextInput(attrs={'class':'form-control'}),
             'Password':forms.PasswordInput(attrs={'class':'form-control','type':'password'}),

         }


class AjouterReservationForm(forms.ModelForm):
    class Meta:
         model = Reservations
         fields = ("dateDebut","dateFin","Prix")
         widgets = {

             'dateDebut':forms.DateInput(attrs={'class':'form-control','type':'date'}),
             'dateFin':forms.DateInput(attrs={'class':'form-control','type':'date'}),
             'Prix':forms.NumberInput(attrs={'class':'form-control'}),
        }

class AjouterPlacesLibresForm(forms.ModelForm):
    class Meta:
         model = PlacesLibres
         fields = ("NombrePlaceDisponible","NombrePlaceReserver")
         widgets = {
             'NombrePlaceDisponible':forms.NumberInput(attrs={'class':'form-control'}),
             'NombrePlaceReserver':forms.NumberInput(attrs={'class':'form-control'}),

        }

class AjouterAbonnementForm(forms.ModelForm):
    class Meta:
         model = Abonnements
         fields = ("TypeAbonnement","DureeAbonnement","Prix")
         widgets = {

             'TypeAbonnement':forms.TextInput(attrs={'class':'form-control'}),
             'DureeAbonnement':forms.TextInput(attrs={'class':'form-control'}),
             'Prix':forms.NumberInput(attrs={'class':'form-control'}),

        }