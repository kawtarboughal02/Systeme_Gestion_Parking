from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import Clients
from .forms import AjouterClientForm
from .models import Reservations
from .forms import AjouterReservationForm
from .models import PlacesLibres
from .forms import AjouterPlacesLibresForm
from .models import Abonnements
from .forms import AjouterAbonnementForm
# Create your views here.

class Accueil(View):
   def get(self,request):
      return  render(request, 'Accueil.html',{})

class About(View):
   def get(self,request):
      return  render(request, 'About.html',{})

def Dashboard(request):
    return render(request,'Dashboard.html')

def Registration(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        Pass1 = request.POST.get('Password1')
        Pass2 = request.POST.get('Password2')

        if Pass1!=Pass2:
            return render(request,'Registration.html',{'error':"Les deux mots de passe ne sont pas identiques."})
        if User.objects.filter(username=uname).exists():
            return render(request,'Registration.html',{'error':"Ce nom d'utilisateur existe déjà."})
        my_user=User.objects.create_user(uname,email,Pass1)
        my_user.save()
        return redirect('Login')

    return render(request,'Registration.html')

def Login(request):
     if request.method=='POST':
         username=request.POST.get('username')
         Pass1=request.POST.get('Password')
         user=authenticate(request,username=username,password=Pass1)
         if user is not None:
             login(request,user)
             return redirect('Dashboard')
         else:
             return render(request,'Login.html',{'error':"Nom d'utilisateur ou mot de passe incorrect."})

     return render(request,'Login.html')

class ListeClients(View):
    def get(self, request):
        cli_data = Clients.objects.all()
        return render(request, 'clients/ListeClients.html',{'clidata':cli_data})


class Ajouter_Client(View):
    def get(self, request):
        fm = AjouterClientForm()
        return render(request,'clients/AjouterClient.html',{'form':fm})

    def post(self, request):
        fm = AjouterClientForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('ListeClients')
        else:
            return render(request, 'clients/AjouterClient.html', {'form': fm})

class Supprimer_Client(View):
    def post(self, request):
        data = request.POST
        code = data.get('code')
        Clidata = Clients.objects.get(code=code)
        Clidata.delete()
        return redirect('ListeClients')
class ModifierClient(View):
    def get(self, request,code):
        cli = Clients.objects.get(code=code)
        fm = AjouterClientForm(instance=cli)
        return render(request,'clients/ModifierClient.html',{'form':fm})

    def post(self,request,code):
        cli = Clients.objects.get(code=code)
        fm = AjouterClientForm(request.POST,instance=cli)
        if fm.is_valid():
            fm.save()
            return redirect('ListeClients')


class ListeReservation(View):
    def get(self, request):
        reservation_data = Reservations.objects.all()
        return render(request, 'Reservation/ListeReservation.html', {'reservationdata': reservation_data})


class Ajouter_Reservation(View):
    def get(self, request):
        fm = AjouterReservationForm()
        return render(request,'Reservation/AjouterReservation.html',{'form': fm})

    def post(self, request):
        fm = AjouterReservationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('ListeReservation')
        else:
            return render(request, 'Reservation/AjouterReservation.html', {'form': fm})


class Supprimer_Reservation(View):
    def post(self, request,id):
        reservationdata = Reservations.objects.get(id=id)
        reservationdata.delete()
        return redirect('ListeReservation')


class ModifierReservation(View):
    def get(self, request, id):
        reservation = Reservations.objects.get(id=id)
        fm = AjouterReservationForm(instance=reservation)
        return render(request, 'Reservation/ModifierReservation.html', {'form': fm})

    def post(self, request, id):
        reservation = Reservations.objects.get(id=id)
        fm = AjouterReservationForm(request.POST, instance=reservation)
        if fm.is_valid():
            fm.save()
            return redirect('ListeReservation')

class ListePlacesLibres(View):
    def get(self, request):
        PlacesLibres_data = PlacesLibres.objects.all()
        return render(request, 'PlacesLibres/ListePlacesLibres.html', {'PlacesLibresdata': PlacesLibres_data})

class Ajouter_PlacesLibres(View):
    def get(self, request):
        fm = AjouterPlacesLibresForm()
        return render(request, 'PlacesLibres/AjouterPlacesLibres.html', {'form': fm})
    def post(self, request):
        fm = AjouterPlacesLibresForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('ListePlacesLibres')
        else:
            return render(request, 'PlacesLibres/AjouterPlacesLibres.html', {'form': fm})

class ModifierPlacesLibres(View):
    def get(self, request, id):
        Places = PlacesLibres.objects.get(id=id)
        fm = AjouterPlacesLibresForm(instance=Places)
        return render(request, 'PlacesLibres/ModifierPlacesLibres.html', {'form': fm})

    def post(self, request, id):
        Places = PlacesLibres.objects.get(id=id)
        fm = AjouterPlacesLibresForm(request.POST, instance=Places)
        if fm.is_valid():
            fm.save()
            return redirect('ListePlacesLibres')


class ListeAbonnement(View):
    def get(self, request):
        Abonnement_data = Abonnements.objects.all()
        return render(request, 'Abonnements/ListeAbonnement.html',{'Abonnementdata':Abonnement_data})


class Ajouter_Abonnement(View):
    def get(self, request):
        fm = AjouterAbonnementForm()
        return render(request,'Abonnements/AjouterAbonnement.html',{'form':fm})

    def post(self, request):
        fm = AjouterAbonnementForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('ListeAbonnement')
        else:
            return render(request, 'Abonnements/AjouterAbonnement.html', {'form': fm})



class ModifierAbonnement(View):
    def get(self, request,id):
        Abonnement = Abonnements.objects.get(id=id)
        fm = AjouterAbonnementForm(instance=Abonnement)
        return render(request,'Abonnements/ModifierAbonnement.html',{'form':fm})

    def post(self,request,id):
        Abonnement = Abonnements.objects.get(id=id)
        fm = AjouterAbonnementForm(request.POST,instance=Abonnement)
        if fm.is_valid():
            fm.save()
            return redirect('ListeAbonnement')
