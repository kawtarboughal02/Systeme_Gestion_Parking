# Guide de publication GitHub — Système de Gestion de Parking

Ce guide rassemble les informations et commandes pour publier le projet sur GitHub.
Le dépôt Git local est déjà initialisé et le premier commit est fait.

---

## 1. Nom du dépôt recommandé

```text
Systeme_Gestion_Parking
```

## 2. Description du dépôt (à copier dans le champ « Description »)

```text
Application web de gestion de parking développée avec Django (MVT) et SQLite : clients, réservations, places et abonnements, avec authentification, tableau de bord et back-office CRUD complet. Base de données relationnelle prête pour la data / l'IA.
```

Version courte (si le champ est limité) :

```text
Application web Django de gestion de parking : clients, réservations, places, abonnements + authentification + CRUD. Data-ready.
```

## 3. Topics (à ajouter dans « Topics »)

```text
django
python
web-application
parking-management
crud
sqlite
bootstrap
mvt
authentication
data-science
```

## 4. Créer le dépôt sur GitHub et pousser le code

### Étape A — Créer le dépôt sur GitHub (interface web)

1. Ouvrir https://github.com/new
2. **Repository name** : `Systeme_Gestion_Parking`
3. **Description** : coller la description de la section 2 ci-dessus.
4. Choisir **Public**.
5. **Ne pas** cocher « Add a README file », ni « Add .gitignore », ni « Choose a license » (le projet en contient déjà).
6. Cliquer sur **Create repository**.

### Étape B — Relier le dépôt local au dépôt distant et pousser

Ouvrir un terminal PowerShell **dans le dossier du projet** et exécuter (remplacer `VOTRE-USERNAME` par `kawtarboughal02`) :

```powershell
cd "c:\Users\bough\Desktop\my drive\Systeme_Gestion_Parking"
git remote add origin https://github.com/kawtarboughal02/Systeme_Gestion_Parking.git
git branch -M main
git push -u origin main
```

> Si GitHub affiche le dépôt avec la branche `master` par défaut et que vous préférez garder `master`, remplacer la 3ᵈ ligne par :
> `git push -u origin master`

### Étape C — Vérifier

Rafraîchir la page du dépôt sur GitHub : le `README.md` doit s'afficher automatiquement, avec les captures d'écran visibles.

---

## 5. Alternative en une commande (si GitHub CLI `gh` est installé)

```powershell
gh repo create kawtarboughal02/Systeme_Gestion_Parking --public --source=. --remote=origin --push --description "Application web Django de gestion de parking : clients, réservations, places, abonnements + authentification + CRUD. Data-ready."
```

Puis ajouter les topics :

```powershell
gh repo edit --add-topic django,python,web-application,parking-management,crud,sqlite,bootstrap,mvt,authentication,data-science
```

---

## 6. Commandes utiles pour les mises à jour suivantes

Après toute modification du projet :

```powershell
git add -A
git commit -m "Description de la modification"
git push
```

## 7. Vérifications avant publication (déjà validées)

- [x] `python manage.py check` → 0 problème
- [x] `python manage.py migrate` → OK
- [x] `python seed_data.py` → 1 admin, 6 clients, 5 réservations, 4 abonnements
- [x] 13 routes testées → toutes en HTTP 200
- [x] 13 captures d'écran générées dans `docs/screenshots/`
- [x] `.gitignore` en place (venv, `db.sqlite3`, `root/` exclus)
- [x] Taille du dépôt : ~4,5 Mo (sous la limite GitHub)
