import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Systeme_Gestion_Parking.settings')
django.setup()
from django.contrib.auth.models import User
from Gestion_Parking.models import Clients, Reservations, PlacesLibres, Abonnements
from datetime import date
from decimal import Decimal
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin','admin@test.com','admin123')
    print('superuser admin cree')
else:
    print("Superutilisateur 'admin' deja present")
for i in range(1,7):
    Clients.objects.get_or_create(code=f'C00{i}', defaults=dict(Nom=f'Nom{i}', Prenom=f'Prenom{i}', email=f'c{i}@test.com', username=f'user{i}', Password='pass123'))
print('6 clients prets')
c1 = Clients.objects.first()
for i in range(1,6):
    Reservations.objects.get_or_create(idReservation=i, defaults=dict(dateDebut=date(2025,1,i), dateFin=date(2025,1,i+1), Prix=Decimal(50+i*10), code=c1))
print('5 reservations pretes')
PlacesLibres.objects.get_or_create(id=1, defaults=dict(NombrePlaceDisponible=80, NombrePlaceReserver=20))
print('Etat des places cree')
for t,d,p in [('Mensuel','30 jours',200),('Trimestriel','90 jours',500),('Semestriel','180 jours',900),('Annuel','365 jours',1500)]:
    Abonnements.objects.get_or_create(TypeAbonnement=t, defaults=dict(DureeAbonnement=d, Prix=Decimal(p)))
print('4 abonnements prets')
print('PEUPLEMENT TERMINE AVEC SUCCES')
