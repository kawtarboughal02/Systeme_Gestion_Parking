# Rapport final — Système de Gestion de Parking

## 1. Résumé exécutif

Ce projet présente une application web de gestion d'un parking, développée avec le framework **Django** (architecture MVT) et une base de données **SQLite**. L'application centralise la gestion de quatre entités métier — **clients**, **réservations**, **places libres** et **abonnements** — et propose une **authentification** (inscription / connexion), un **tableau de bord** et un **back-office** complet (ajout, consultation, modification, suppression) pour chaque entité.

Le projet couvre l'ensemble de la chaîne : analyse des besoins, conception du modèle de données, implémentation des vues et formulaires Django, mise en place de l'authentification, gestion des migrations, peuplement d'un jeu de démonstration et validation automatisée.

La validation locale confirme le bon fonctionnement : `manage.py check` ne remonte aucune anomalie, les migrations s'appliquent sans erreur, le jeu de démonstration est peuplé (1 administrateur, 6 clients, 5 réservations, 1 état des places, 4 abonnements) et les **13 routes** de l'application répondent toutes en **HTTP 200**. Treize captures d'écran documentent les interfaces.

La base de données relationnelle produite constitue, par ailleurs, un **jeu de données structuré** directement exploitable pour de futurs traitements data et des modèles d'intelligence artificielle (prévision de la demande, tarification dynamique, détection d'anomalies).

## 2. Contexte, objectif et problématique

La gestion manuelle d'un parking — suivi des places, des réservations, des abonnés et des encaissements — repose fréquemment sur des tableurs dispersés ou des registres papier. Cette organisation engendre des risques concrets : **double saisie**, **pertes d'information**, **rupture de traçabilité** et difficulté à produire des indicateurs fiables sur l'occupation et les revenus.

**Objectif :** concevoir et implémenter une application web unique, fiable et traçable, qui centralise la gestion quotidienne d'un parking et fournit une base de données propre, prête à alimenter des analyses et des modèles d'IA.

**Problématique :** comment centraliser et fiabiliser la gestion des clients, des réservations, des places et des abonnements au sein d'une même application, tout en garantissant l'authentification des utilisateurs, la traçabilité des opérations et l'exploitabilité future des données ?

## 3. Données et modèle métier

L'application s'appuie sur l'**ORM Django** et une base **SQLite**. Quatre modèles métier structurent les données :

| Modèle | Rôle | Champs principaux |
|---|---|---|
| `Clients` | Personne cliente du parking | `code`, `Nom`, `Prenom`, `email`, `username`, `Password`, `user` (FK vers `auth.User`) |
| `Reservations` | Réservation d'une place sur une période | `idReservation`, `dateDebut`, `dateFin`, `Prix`, `code` (FK vers `Clients`) |
| `PlacesLibres` | État courant des places | `NombrePlaceDisponible`, `NombrePlaceReserver` |
| `Abonnements` | Formules d'abonnement | `TypeAbonnement`, `DureeAbonnement`, `Prix` |

**Relations :**
- `Reservations.code` → clé étrangère vers `Clients` (`on_delete=SET_NULL`).
- `Clients.user` → clé étrangère vers `auth.User` (`on_delete=SET_NULL`).

**Authentification :** la connexion et l'inscription réelles s'appuient sur `django.contrib.auth` (table `auth_user`). La table métier `Clients` comporte en plus des champs `username` et `Password` utilisés dans le formulaire de démonstration ; **ils ne constituent pas le mécanisme d'authentification**, ce point étant traité dans les limites (§8).

**Jeu de démonstration (`seed_data.py`)** : création idempotente (`get_or_create`) de 1 superutilisateur (`admin`), 6 clients, 5 réservations, 1 état des places et 4 abonnements. Les données sont fictives.

Le schéma de la base est versionné par trois migrations (`0001`, `0002`, `0003`), garantissant la reproductibilité.

## 4. Méthodologie

### 4.1 Analyse des besoins et conception

Identification des entités métier (clients, réservations, places, abonnements), des parcours utilisateur (consultation publique, authentification, back-office) et des relations entre entités. Le modèle de données est implémenté via les modèles Django, et l'organisation du code suit le patron **MVT** (Model – View – Template) propre au framework.

### 4.2 Implémentation

- **Modèles (`models.py`)** : définition des quatre entités et de leurs relations.
- **Formulaires (`forms.py`)** : `ModelForm` Django pour chaque entité, avec widgets Bootstrap (`form-control`) et validation intégrée.
- **Vues (`views.py`)** : vues fondées sur les classes (`View`) pour le CRUD, et vues fonctions pour l'authentification (`Registration`, `Login`) et le `Dashboard`.
- **Routage (`urls.py`)** : routes nommées pour chaque page, organisées entre l'application `Gestion_Parking` et la configuration du projet `Systeme_Gestion_Parking`.
- **Templates** : 16 templates HTML utilisant **Bootstrap 5** et **Font Awesome**, avec un en-tête commun (`header.html`) et des dossiers par entité (`clients/`, `Reservation/`, `PlacesLibres/`, `Abonnements/`).
- **Administration (`admin.py`)** : enregistrement des quatre modèles dans le back-office Django.

### 4.3 Authentification

- **Inscription** : création d'un utilisateur via `User.objects.create_user`, avec vérification de l'unicité du nom d'utilisateur et de la correspondance des mots de passe.
- **Connexion** : authentification via `authenticate()` puis `login()`, avec redirection vers le tableau de bord en cas de succès et message d'erreur explicite en cas d'échec.

### 4.4 Peuplement et validation

- **Peuplement** : `seed_data.py` (complet) et `seed_demo.py` (variante compacte), tous deux idempotents.
- **Validation** : `manage.py check` (intégrité du projet), `manage.py migrate` (schéma de base), test HTTP de l'ensemble des routes et captures d'écran automatisées via Playwright.



## 5. Résultats et validation

Le projet a été testé localement dans l'environnement suivant : **Python 3.13.7**, **Django 5.1.15**, **SQLite**. (Le projet est également compatible avec Django 4.1.7, version référencée dans `requirements.txt`.)

| Contrôle | Commande | Résultat |
|---|---|---|
| Intégrité du projet | `python manage.py check` | Aucune anomalie (0 problème) |
| Schéma de base | `python manage.py migrate` | Migrations appliquées avec succès |
| Peuplement | `python seed_data.py` | 1 admin, 6 clients, 5 réservations, 1 état des places, 4 abonnements |
| Test HTTP des routes | Requêtes sur 13 URL | **Toutes en HTTP 200** |

**Détail du test HTTP (routes validées) :**

| Route | Code HTTP | Taille de réponse |
|---|---:|---:|
| `/` (Accueil) | 200 | ~4,8 Ko |
| `/About` | 200 | ~7,2 Ko |
| `/Login` | 200 | ~3,3 Ko |
| `/Registration` | 200 | ~3,5 Ko |
| `/Dashboard` | 200 | ~3,1 Ko |
| `/ListeClients` | 200 | ~11,7 Ko |
| `/AjouterClient` | 200 | ~2,5 Ko |
| `/ListeReservation` | 200 | ~9,4 Ko |
| `/AjouterReservation` | 200 | ~2,0 Ko |
| `/ListePlacesLibres` | 200 | ~4,2 Ko |
| `/AjouterPlacesLibres` | 200 | ~1,9 Ko |
| `/ListeAbonnement` | 200 | ~6,3 Ko |
| `/AjouterAbonnement` | 200 | ~2,0 Ko |

**Observation de validation :** au cours des tests, un serveur résiduel d'un autre projet (PHP) occupait le port 8000 et renvoyait des erreurs 404. Après libération du port et exécution sur un port dédié, l'ensemble des routes répond correctement. Ce point illustre l'importance de vérifier qu'aucun autre service n'occupe le port avant de lancer ou de tester l'application — un réflexe de débogage à documenter.

## 6. Application web et interfaces

Le schéma ci-dessous résume l'architecture MVT et les flux de l'application :

```text
Navigateur (client)
        │  HTTP
        ▼
URLconf (Systeme_Gestion_Parking/urls.py + Gestion_Parking/urls.py)
        │
        ▼
Vues Django (views.py) ──► Formulaires (forms.py) ──► ORM ──► SQLite
        │                                                      (Clients,
        ▼                                                       Reservations,
Templates (Bootstrap 5)                                        PlacesLibres,
        │                                                       Abonnements)
        ▼
Pages rendues + Admin Django (/admin)
```

**Routes principales exposées :**

| Route | Vue | Fonction |
|---|---|---|
| `/` | `Accueil` | Page d'accueil publique |
| `/About` | `About` | Présentation de la solution |
| `/Registration` | `Registration` | Création de compte |
| `/Login` | `Login` | Connexion |
| `/Dashboard` | `Dashboard` | Tableau de bord (menu latéral) |
| `/ListeClients`, `/AjouterClient`, `/ModifierClient/<code>/` | vues CRUD Clients | Gestion des clients |
| `/ListeReservation`, `/AjouterReservation`, `/ModifierReservation/<id>/`, `/SupprimerReservation/<id>/` | vues CRUD Réservations | Gestion des réservations |
| `/ListePlacesLibres`, `/AjouterPlacesLibres`, `/ModifierPlacesLibres/<id>/` | vues CRUD Places | État des places |
| `/ListeAbonnement`, `/AjouterAbonnement`, `/ModifierAbonnement/<id>/` | vues CRUD Abonnements | Formules d'abonnement |
| `/admin` | admin Django | Back-office intégré |

**Interfaces (13 captures d'écran) :** chaque interface a été photographiée automatiquement et est documentée dans le [README](./README.md#captures-d%C3%A9cran-des-interfaces) et dans le dossier `docs/screenshots/` : accueil, à propos, connexion, inscription, tableau de bord, puis les pages Liste / Ajouter des clients, réservations, places et abonnements.

## 7. Technologies

| Technologie | Rôle |
|---|---|
| Python | Langage de programmation principal |
| Django (MVT, ORM, auth) | Framework web, mapping objet-relationnel, authentification |
| SQLite | Base de données relationnelle (développement) |
| Django Forms + CSRF | Formulaires, validation et protection contre les attaques CSRF |
| Bootstrap 5 | Framework CSS responsive |
| Font Awesome | Bibliothèque d'icônes |
| HTML / CSS | Templates et mise en page |
| Playwright | Capture automatisée des interfaces |
| Git / GitHub | Versionnement et publication du code |



## 8. Limites et considérations éthiques

1. **Mots de passe de démonstration en clair** : la table métier `Clients` stocke les champs `username` et `Password` en clair (usage pédagogique). L'authentification réelle passe par `auth_user` de Django, mais cette double table doit être corrigée (hachage, suppression des doublons) avant tout usage réel.
2. **Gestion des rôles limitée** : pas de RBAC fin (administrateur / agent / client). Toutes les pages du back-office sont accessibles sans contrôle de permission.
3. **Pas de pagination ni de recherche serveur** : les listes chargent l'ensemble des enregistrements ; la barre de recherche de l'en-tête n'est pas fonctionnelle côté serveur.
4. **Configuration de développement** : `DEBUG=True`, `SECRET_KEY` codée en dur, `ALLOWED_HOSTS` vide, SQLite en mono-poste.
5. **Données fictives** : le jeu de démonstration ne représente pas un cas d'usage réel.
6. **Suppression non confirmée** : les actions de suppression s'effectuent sans modale de confirmation.
7. **Protection des données personnelles** : les données clients (nom, e-mail) nécessiteraient, en production, une conformité RGPD (chiffrement, durée de conservation, base légale).

**Avant un usage en production**, il faudrait : hacher les mots de passe, mettre en place un RBAC, migrer vers PostgreSQL, activer HTTPS, externaliser la `SECRET_KEY`, désactiver `DEBUG`, ajouter la pagination et la recherche, et encadrer le traitement des données personnelles.

## 9. Lien Data Scientist / IA

L'application génère une **base relationnelle structurée** (occupation des places, durées et périodes de réservation, prix, formules d'abonnement, profils clients). Ces données constituent un **jeu de données naturel** pour des traitements analytiques et des modèles d'intelligence artificielle. Extensions envisageables :

- **Tableau de bord analytique** (Pandas / Matplotlib / Seaborn) : taux d'occupation, revenus par période, répartition par formule d'abonnement.
- **Prévision de la demande et de l'affluence** : modèles de séries temporelles ou de régression (type XGBoost) pour anticiper les pics d'occupation.
- **Détection d'anomalies** : identification de réservations ou de paiements atypiques.
- **Tarification dynamique** : ajustement des prix selon l'occupation et la période.
- **OCR de plaques d'immatriculation** : entrée / sortie automatique des véhicules.
- **Chatbot de réservation** : assistant conversationnel exploitant l'historique client.

Ces pistes transforment l'application d'un simple outil de gestion en une **plateforme data-ready**, créant un pont direct vers les compétences d'un Data Scientist.

## 10. Reproductibilité et exécution

Installer l'environnement et lancer l'application :

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python seed_data.py
python manage.py runserver
```

Vérifier l'intégrité et peupler :

```powershell
python manage.py check      # doit indiquer 0 problème
python seed_data.py         # crée admin + 6 clients + 5 réservations + 4 abonnements
```

Régénérer les captures d'écran :

```powershell
python -m pip install playwright
python capture_screenshots.py
```

Le script `capture_screenshots.py` démarre le serveur Django, photographie chaque interface via Playwright (en utilisant le navigateur Chrome déjà installé sur le système), puis arrête le serveur. Les images sont enregistrées dans `docs/screenshots/`.

**Adresses utiles :**

| Page | Adresse |
|---|---|
| Accueil | http://127.0.0.1:8000/ |
| Connexion | http://127.0.0.1:8000/Login |
| Tableau de bord | http://127.0.0.1:8000/Dashboard |
| Admin Django | http://127.0.0.1:8000/admin |

Compte administrateur de démonstration : **admin** / **Admin@123**.

## 11. Conclusion et perspectives

Le projet délivre une application web fonctionnelle, testée et documentée pour la gestion d'un parking. Il met en œuvre les briques fondamentales d'une application Django — modèles, vues, formulaires, authentification, migrations et administration — autour de quatre entités métier, avec un back-office complet et une validation automatisée.

La validation locale confirme un socle stable : aucune anomalie au `check`, migrations appliquées, jeu de démonstration peuplé et 13 routes opérationnelles. La base de données relationnelle produite est **propre et structurée**, ce qui en fait un point d'ancrage naturel pour des traitements data et des modèles d'IA.

**Perspectives d'amélioration prioritaires :**
1. Hachage des mots de passe et suppression de la duplication d'authentification.
2. Mise en place d'un RBAC (administrateur / agent / client).
3. Pagination et recherche côté serveur.
4. Migration vers PostgreSQL et durcissement de la configuration pour un déploiement en production.
5. Branchement d'un module analytique (dashboard Pandas) puis de modèles prédictifs (prévision d'affluence, tarification dynamique).

## English summary

This project is a **Django** car-park management web application (MVT, SQLite). It centralizes four business entities — clients, bookings, available spaces and subscriptions — with authentication, a dashboard and a full CRUD back-office. Local validation confirms a stable foundation: `manage.py check` reports no issues, migrations apply cleanly, the demo dataset is seeded (1 admin, 6 clients, 5 bookings, 1 spaces state, 4 subscriptions) and all 13 routes return HTTP 200. Thirteen screenshots document the interfaces. The clean relational data produced is a natural dataset for future data/AI work (occupancy analytics, demand forecasting, dynamic pricing, anomaly detection). Key next steps: password hashing, role-based access control, pagination/search, and a PostgreSQL-based production configuration.

