# Gestion Immo

![Django](https://img.shields.io/badge/Django-5.0-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge&logo=mysql)

Application Django moderne de gestion de location immobilière avec catalogue, réservation et interface d'administration.

## 📋 Description

**Gestion Immo** est une plateforme web complète pour la gestion de locations immobilières en Guinée. Le projet permet aux utilisateurs de :

- Consulter un catalogue de logements avec recherche et filtrage
- Visualiser les détails de chaque logement (photos, équipements, prix)
- Effectuer des réservations en ligne avec validation de paiement
- Gérer les réservations et les logements via un tableau de bord sécurisé

Le projet a fait l'objet d'une refonte UI/UX complète avec un design moderne, des animations fluides et une expérience utilisateur optimisée.

## ✨ Caractéristiques

### Frontend (Public)
- **Page d'accueil** : Hero section animée, logements en vedette, FAQ interactif
- **Catalogue de logements** : Recherche par critères, filtrage, pagination
- **Détail de logement** : Galerie photos interactive, calcul de prix dynamique, avis clients
- **Formulaire de réservation** : Validation des dates, simulation de paiement sécurisé
- **Page contact** : Formulaire de contact, FAQ, informations de contact

### Dashboard (Administration)
- **Tableau de bord** : Statistiques en temps réel, dernières réservations
- **Gestion des logements** : CRUD complet, upload d'images, gestion des disponibilités
- **Gestion des réservations** : Suivi des réservations, validation, annulation
- **Paramètres** : Gestion du compte utilisateur

### Design System
- Palette de couleurs moderne avec gradients
- Typographie Inter et Poppins
- Micro-interactions et animations fluides
- Design responsive (mobile-first)
- Accessibilité (WCAG AA)

## 🚀 Installation

### Prérequis

- Python 3.13+
- MySQL 8.0+ (ou PostgreSQL/SQLite pour développement)
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le dépôt**
```bash
git clone <repository-url>
cd Gestion_Immo
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
python -m pip install -r requirements.txt
```

4. **Configurer la base de données**

Le projet utilise MySQL par défaut. Modifiez `config/settings.py` selon votre configuration :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gestion_immo',
        'USER': 'votre_utilisateur',
        'PASSWORD': 'votre_mot_de_passe',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

Pour utiliser SQLite (développement), décommentez le bloc `sqlite3` dans `config/settings.py`.

5. **Créer la base de données MySQL**
```sql
CREATE DATABASE gestion_immo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

6. **Appliquer les migrations**
```bash
python manage.py migrate
```

7. **Créer un superutilisateur**
```bash
python manage.py createsuperuser
```

8. **Lancer le serveur**
```bash
python manage.py runserver
```

Ouvrez `http://127.0.0.1:8000/` dans votre navigateur.

## 🧪 Tests

Le projet inclut des tests unitaires et fonctionnels pour les formulaires, modèles et vues principales.

Les tests utilisent SQLite automatiquement pour isoler les tests de la base de données de production.

```bash
# Exécuter tous les tests
python manage.py test

# Exécuter les tests d'une application spécifique
python manage.py test principale
python manage.py test dashboard

# Exécuter avec verbosité
python manage.py test --verbosity=2
```

## 📁 Structure du projet

```
Gestion_Immo/
├── config/                 # Configuration Django
│   ├── settings.py       # Paramètres principaux
│   ├── urls.py           # URL routing global
│   └── wsgi.py           # Configuration WSGI
├── principale/           # Application front-office
│   ├── models.py         # Modèles (Logement, Image, Reservation)
│   ├── forms.py          # Formulaires de réservation
│   ├── views.py          # Vues publiques
│   ├── urls.py           # URL routing principale
│   ├── static/           # Fichiers statiques (CSS, JS, images)
│   │   └── css/
│   │       └── styles.css  # Design system complet
│   └── templates/        # Templates HTML
│       └── principale/
│           ├── base.html
│           ├── home.html
│           ├── listings.html
│           ├── listing_detail.html
│           ├── about.html
│           ├── contact.html
│           ├── reservation.html
│           └── confirmation.html
├── dashboard/            # Application back-office
│   ├── models.py         # Modèles (Client)
│   ├── forms.py          # Formulaires admin
│   ├── views.py          # Vues dashboard
│   ├── urls.py           # URL routing dashboard
│   └── templates/
│       └── dashboard/
│           ├── base.html
│           ├── index.html
│           ├── logements.html
│           ├── logement_form.html
│           ├── reservations.html
│           ├── reservation_detail.html
│           ├── parametres.html
│           └── login.html
├── requirements.txt      # Dépendances Python
├── manage.py            # Script de gestion Django
├── README.md            # Ce fichier
└── PRESENTATION.md      # Documentation détaillée du projet
```

## 🎨 Design System

Le projet utilise un design system moderne avec :

- **Couleurs primaires** : #FF6B6B (corail), #4ECDC4 (turquoise)
- **Couleurs secondaires** : #FFE66D (jaune), #1A1A2E (bleu nuit)
- **Typographie** : Inter (body), Poppins (headings)
- **Espacement** : Système de variables CSS
- **Ombres** : Subtiles à fortes pour la profondeur
- **Transitions** : 300ms cubic-bezier pour fluidité
- **Bordures** : Coins arrondis (8px à 24px)

## 🔐 Sécurité

- Authentification Django intégrée
- Protection CSRF sur tous les formulaires
- Validation des entrées utilisateur
- Protection contre les injections SQL (ORM Django)
- Gestion des sessions sécurisée

## 🌐 Technologies Utilisées

- **Backend** : Django 5.0, Python 3.13
- **Base de données** : MySQL 8.0
- **Frontend** : HTML5, CSS3, JavaScript (ES6+)
- **Icônes** : Lucide Icons
- **Police** : Google Fonts (Inter, Poppins)

## 📝 Points de validation

- ✅ Validation des dates de réservation (arrivée < départ)
- ✅ Validation du numéro de carte bancaire (Luhn)
- ✅ Validation de la date d'expiration de la carte
- ✅ Calcul automatique du montant total
- ✅ Détection des chevauchements de réservations
- ✅ Redirection des utilisateurs non authentifiés
- ✅ Tests unitaires et fonctionnels

## 🔧 Améliorations futures

- Intégration d'un véritable système de paiement (Stripe/PayPal)
- Notifications par email pour les réservations
- Système de reviews et ratings pour les logements
- Recherche géolocalisée avec carte interactive
- API REST pour intégration mobile
- Système de messagerie entre propriétaires et locataires

## 👥 Auteurs

Projet réalisé dans le cadre d'un cours de développement web.

## 📄 Licence

Ce projet est à usage éducatif.
