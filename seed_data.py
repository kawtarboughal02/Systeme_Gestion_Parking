"""
Script de peuplement de la base avec des donnees de demonstration.
Usage : python seed_data.py
"""
import os
import django
from datetime import date, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Systeme_Gestion_Parking.settings")
django.setup()

from django.contrib.auth.models import User
from Gestion_Parking.models import Clients, Reservations, PlacesLibres, Abonnements

# 1) Superutilisateur / administrateur
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@parking.ma", "Admin@123")
    print("Superutilisateur 'admin' cree (mot de passe : Admin@123)")
else:
    print("Superutilisateur 'admin' deja present")

# 2) Clients
clients_data = [
    ("C001", "Boughal", "Kawtar", "kawtar.boughal@example.com", "kawtar", "kawtar123"),
    ("C002", "El Amrani", "Youssef", "youssef.amrani@example.com", "youssef", "youssef123"),
    ("C003", "Benali", "Salma", "salma.benali@example.com", "salma", "salma123"),
    ("C004", "Ouahbi", "Mehdi", "mehdi.ouahbi@example.com", "mehdi", "mehdi123"),
    ("C005", "Chraibi", "Nadia", "nadia.chraibi@example.com", "nadia", "nadia123"),
    ("C006", "Tazi", "Omar", "omar.tazi@example.com", "omar", "omar123"),
]

clients = []
for code, nom, prenom, email, username, pwd in clients_data:
    client, created = Clients.objects.get_or_create(
        code=code,
        defaults={
            "Nom": nom,
            "Prenom": prenom,
            "email": email,
            "username": username,
            "Password": pwd,
        },
    )
    clients.append(client)
    # creer aussi un compte de connexion Django pour demonstrer l'authentification
    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username, email, pwd)
print(f"{len(clients)} clients prets")

# 3) Reservations
today = date.today()
reservations_data = [
    (1001, today + timedelta(days=1), today + timedelta(days=3), 150.00, clients[0]),
    (1002, today + timedelta(days=2), today + timedelta(days=5), 220.50, clients[1]),
    (1003, today + timedelta(days=4), today + timedelta(days=6), 180.00, clients[2]),
    (1004, today + timedelta(days=7), today + timedelta(days=10), 300.75, clients[3]),
    (1005, today + timedelta(days=12), today + timedelta(days=15), 260.00, clients[4]),
]
for idr, d1, d2, prix, client in reservations_data:
    Reservations.objects.get_or_create(
        idReservation=idr,
        defaults={"dateDebut": d1, "dateFin": d2, "Prix": prix, "code": client},
    )
print(f"{len(reservations_data)} reservations pretes")

# 4) Places libres
PlacesLibres.objects.get_or_create(
    NombrePlaceDisponible=42,
    NombrePlaceReserver=18,
)
print("Etat des places libres cree")

# 5) Abonnements
abonnements_data = [
    ("Abonnement Journalier", "1 jour", 15.00),
    ("Abonnement Hebdomadaire", "7 jours", 80.00),
    ("Abonnement Mensuel", "30 jours", 300.00),
    ("Abonnement Annuel", "365 jours", 3000.00),
]
for type_ab, duree, prix in abonnements_data:
    Abonnements.objects.get_or_create(
        TypeAbonnement=type_ab,
        defaults={"DureeAbonnement": duree, "Prix": prix},
    )
print(f"{len(abonnements_data)} abonnements prets")

print("PEUPLEMENT TERMINE AVEC SUCCES")
