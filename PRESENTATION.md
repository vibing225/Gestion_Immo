# Gestion Immo - Documentation de Projet

## Table des matières

1. [Introduction](#introduction)
2. [Contexte et Objectifs](#contexte-et-objectifs)
3. [Architecture Technique](#architecture-technique)
4. [Base de Données](#base-de-données)
5. [Fonctionnalités](#fonctionnalités)
6. [Design System et UI/UX](#design-system-et-uiux)
7. [Sécurité](#sécurité)
8. [Tests](#tests)
9. [Déploiement](#déploiement)
10. [Conclusion](#conclusion)

---

## Introduction

**Gestion Immo** est une application web complète de gestion de locations immobilières développée avec Django. Ce projet a été réalisé dans le cadre d'un cours de développement web avec pour objectif de créer une plateforme moderne permettant aux utilisateurs de consulter, réserver et gérer des logements.

### Problématique

Le marché immobilier en Guinée manque d'une plateforme centralisée et moderne permettant aux utilisateurs de :
- Consulter facilement des logements disponibles
- Effectuer des réservations en ligne
- Gérer leurs réservations de manière intuitive

### Solution

Gestion Immo offre une solution complète avec :
- Une interface publique moderne et intuitive pour les utilisateurs
- Un tableau de bord administratif pour la gestion
- Un système de réservation avec validation
- Un design soigné et responsive

---

## Contexte et Objectifs

### Objectifs Principaux

1. **Catalogue de Logements** : Permettre aux utilisateurs de parcourir un catalogue de logements avec recherche et filtrage
2. **Système de Réservation** : Implémenter un système de réservation en ligne avec validation des dates et simulation de paiement
3. **Interface d'Administration** : Créer un tableau de bord pour gérer les logements et les réservations
4. **Expérience Utilisateur** : Offrir une interface moderne, responsive et intuitive

### Contraintes

- Utilisation de Django comme framework backend
- Base de données MySQL
- Interface responsive (mobile-first)
- Validation des données côté serveur et client
- Tests unitaires et fonctionnels

---

## Architecture Technique

### Stack Technologique

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend                            │
├─────────────────────────────────────────────────────────┤
│  HTML5  │  CSS3  │  JavaScript (ES6+)  │  Lucide Icons │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│              Django Framework (Backend)                 │
├─────────────────────────────────────────────────────────┤
│  Views  │  Models  │  Forms  │  Templates  │  URLs     │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│              Base de Données MySQL                       │
├─────────────────────────────────────────────────────────┤
│  Logements  │  Images  │  Réservations  │  Clients     │
└─────────────────────────────────────────────────────────┘
```

### Structure des Applications Django

Le projet est divisé en deux applications principales :

#### 1. Application `principale` (Frontend)

Cette application gère toutes les pages publiques accessibles aux utilisateurs :

- **Modèles** :
  - `Logement` : Représente un logement avec ses caractéristiques
  - `Image` : Stocke les images associées à un logement
  - `Reservation` : Gère les réservations avec dates, montant et statut

- **Vues** :
  - `home` : Page d'accueil avec logements en vedette
  - `listings` : Catalogue de logements avec recherche et filtrage
  - `listing_detail` : Page de détail d'un logement
  - `reservation` : Formulaire de réservation
  - `confirmation` : Page de confirmation après réservation
  - `about` : Page à propos
  - `contact` : Page de contact

- **Formulaires** :
  - `ReservationForm` : Validation des dates de réservation
  - `PaiementForm` : Simulation de paiement avec validation de carte

#### 2. Application `dashboard` (Backend)

Cette application gère le tableau de bord administratif :

- **Modèles** :
  - `Client` : Informations des clients (nom, email, téléphone)

- **Vues** :
  - `index` : Tableau de bord avec statistiques
  - `logements` : Liste des logements avec actions CRUD
  - `logement_form` : Création/modification de logement
  - `reservations` : Liste des réservations avec gestion
  - `reservation_detail` : Détail et validation de réservation
  - `parametres` : Paramètres du compte
  - `login` : Connexion au dashboard

- **Formulaires** :
  - `LogementForm` : Création/modification de logement
  - `ReservationStatusForm` : Changement de statut de réservation

### Pattern MVT (Model-View-Template)

Django utilise le pattern MVT qui est une variante de MVC :

- **Model** : Gère la structure des données et les interactions avec la base de données
- **View** : Traite les requêtes HTTP, interagit avec les modèles et renvoie les templates
- **Template** : Génère le HTML envoyé au navigateur

```python
# Exemple de flux MVT
URL Request → View (logique métier) → Model (données) → Template (HTML) → Response
```

---

## Base de Données

### Schéma Relationnel

```
┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│   Logement   │         │    Image     │         │  Reservation │
├──────────────┤         ├──────────────┤         ├──────────────┤
│ id (PK)      │         │ id (PK)      │         │ id (PK)      │
│ titre        │         │ logement_id  │◄────────│ logement_id  │
│ description  │         │ image        │         │ client_id    │
│ adresse      │         └──────────────┘         │ date_arrivee │
│ ville        │                                  │ date_depart  │
│ prix_par_nuit│                                  │ montant_total│
│ capacite     │         ┌──────────────┐         │ statut       │
│ created_at   │         │    Client    │         └──────────────┘
└──────────────┘         ├──────────────┤
                         │ id (PK)      │
                         │ nom          │
                         │ email        │
                         │ telephone    │
                         └──────────────┘
```

### Modèles Détaillés

#### Logement

```python
class Logement(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    prix_par_nuit = models.DecimalField(max_digits=10, decimal_places=2)
    capacite = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
```

**Champs** :
- `titre` : Nom du logement
- `description` : Description détaillée
- `adresse` : Adresse physique
- `ville` : Ville
- `prix_par_nuit` : Prix par nuit en GNF
- `capacite` : Nombre de personnes maximum
- `created_at` : Date de création

#### Image

```python
class Image(models.Model):
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='logements/')
```

**Relation** : Chaque logement peut avoir plusieurs images (relation One-to-Many)

#### Reservation

```python
class Reservation(models.Model):
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_arrivee = models.DateField()
    date_depart = models.DateField()
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
```

**Statuts possibles** :
- `EN_ATTENTE` : Réservation en attente de validation
- `CONFIRMEE` : Réservation confirmée
- `ANNULEE` : Réservation annulée

**Validation** :
- La date de départ doit être postérieure à la date d'arrivée
- Détection des chevauchements avec les réservations confirmées

#### Client

```python
class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
```

### Migrations Django

Les migrations Django permettent de gérer les changements de schéma de base de données :

```bash
# Créer les migrations après modification des modèles
python manage.py makemigrations

# Appliquer les migrations à la base de données
python manage.py migrate
```

---

## Fonctionnalités

### Frontend (Public)

#### 1. Page d'Accueil

**Composants** :
- Hero section avec image de fond et appel à l'action
- Barre de recherche rapide
- Section "À propos" avec icônes
- Logements en vedette (cards modernes)
- FAQ interactif avec accordéon
- Footer avec liens et informations

**Fonctionnalités JavaScript** :
- Accordéon FAQ avec rotation d'icône
- Navigation mobile responsive

#### 2. Catalogue de Logements

**Fonctionnalités** :
- Affichage en grille de tous les logements
- Recherche par titre, ville
- Filtrage par prix (min/max)
- Filtrage par capacité
- Pagination pour les grands volumes

**Design** :
- Cards modernes avec image, titre, prix, ville
- Hover effects avec élévation
- Badges pour les statuts de disponibilité

#### 3. Détail de Logement

**Composants** :
- Galerie photos interactive (main image + thumbnails)
- Informations détaillées (titre, description, adresse)
- Grille d'équipements avec icônes
- Carte de réservation avec calcul de prix dynamique
- Section emplacement (placeholder pour carte interactive)
- Avis clients

**Fonctionnalités JavaScript** :
- Clic sur thumbnail pour changer l'image principale
- Calcul automatique du prix total (prix × nuits + frais)

#### 4. Formulaire de Réservation

**Validation Côté Client** :
- Vérification que la date de départ > date d'arrivée
- Validation du numéro de carte (algorithme de Luhn)
- Validation de la date d'expiration
- Validation du CVC (3 ou 4 chiffres)

**Validation Côté Serveur** :
- Vérification des dates
- Détection des chevauchements avec réservations confirmées
- Création automatique du client si inexistant

#### 5. Page Contact

**Composants** :
- Cartes de contact (téléphone, email, localisation, horaires)
- Formulaire de contact avec icônes
- FAQ avec accordéon
- Section emplacement

**Fonctionnalités JavaScript** :
- Accordéon FAQ avec rotation d'icône

### Dashboard (Administration)

#### 1. Tableau de Bord

**Statistiques affichées** :
- Nombre total de logements
- Nombre total de réservations
- Réservations en attente
- Réservations confirmées
- Réservations annulées
- Revenus estimés

**Dernières réservations** :
- Tableau avec les 5 dernières réservations
- Colonnes : Client, Logement, Dates, Montant, Statut

#### 2. Gestion des Logements

**Actions disponibles** :
- Liste de tous les logements
- Création d'un nouveau logement
- Modification d'un logement existant
- Suppression d'un logement
- Upload d'images multiples

**Formulaire de logement** :
- Titre, description, adresse, ville
- Prix par nuit, capacité
- Upload d'images

#### 3. Gestion des Réservations

**Actions disponibles** :
- Liste de toutes les réservations
- Filtrage par statut
- Validation de réservation (EN_ATTENTE → CONFIRMEE)
- Annulation de réservation
- Détail d'une réservation

**Workflow de validation** :
1. Client effectue une réservation → Statut : EN_ATTENTE
2. Administrateur valide → Statut : CONFIRMEE
3. Ou administrateur annule → Statut : ANNULEE

#### 4. Authentification

**Système de connexion** :
- Formulaire de login avec username/password
- Utilisation du système d'authentification Django
- Protection des pages dashboard avec `@login_required`
- Redirection automatique si non authentifié

---

## Design System et UI/UX

### Philosophie de Design

Le design system a été créé avec les principes suivants :
- **Modernité** : Utilisation de couleurs vives et de gradients
- **Clarté** : Hiérarchie visuelle claire avec typographie variée
- **Accessibilité** : Contrastes respectés, tailles de police lisibles
- **Fluidité** : Transitions et animations douces
- **Cohérence** : Variables CSS pour la maintenance

### Palette de Couleurs

```css
/* Couleurs Primaires */
--color-primary: #FF6B6B;        /* Corail vibrant */
--color-primary-dark: #EE5A5A;   /* Corail foncé */
--color-primary-light: #FF8E8E;   /* Corail clair */

/* Couleurs Secondaires */
--color-secondary: #4ECDC4;       /* Turquoise */
--color-accent: #FFE66D;          /* Jaune soleil */

/* Couleurs Sombres */
--color-dark: #1A1A2E;            /* Bleu nuit profond */
--color-dark-light: #16213E;      /* Bleu nuit clair */
--color-dark-medium: #0F3460;     /* Bleu moyen */

/* Couleurs Claires */
--color-light: #F8F9FA;           /* Blanc cassé */
--color-light-medium: #E9ECEF;    /* Gris très clair */
--color-light-dark: #DEE2E6;       /* Gris clair */

/* Couleurs de Texte */
--color-text: #2D3436;            /* Gris foncé */
--color-text-light: #636E72;      /* Gris moyen */
--color-text-lighter: #B2BEC3;    /* Gris clair */

/* Couleurs Fonctionnelles */
--color-success: #00B894;         /* Vert émeraude */
--color-warning: #FDCB6E;         /* Jaune ambre */
--color-danger: #FF7675;          /* Rouge corail */
--color-info: #74B9FF;            /* Bleu ciel */
```

### Typographie

```css
/* Polices */
--font-body: 'Inter', sans-serif;
--font-heading: 'Poppins', sans-serif;

/* Tailles de police */
--text-xs: 0.75rem;      /* 12px */
--text-sm: 0.875rem;     /* 14px */
--text-base: 1rem;       /* 16px */
--text-lg: 1.125rem;     /* 18px */
--text-xl: 1.25rem;      /* 20px */
--text-2xl: 1.5rem;      /* 24px */
--text-3xl: 1.875rem;    /* 30px */
--text-4xl: 2.25rem;     /* 36px */
```

### Système d'Espacement

```css
/* Unités d'espacement */
--space-1: 0.25rem;      /* 4px */
--space-2: 0.5rem;       /* 8px */
--space-3: 0.75rem;      /* 12px */
--space-4: 1rem;         /* 16px */
--space-6: 1.5rem;        /* 24px */
--space-8: 2rem;         /* 32px */
--space-12: 3rem;        /* 48px */
--space-16: 4rem;        /* 64px */
--space-24: 6rem;        /* 96px */
```

### Ombres

```css
/* Niveaux d'ombre */
--shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.06);
--shadow-md: 0 4px 16px rgba(0, 0, 0, 0.08);
--shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.12);
--shadow-xl: 0 16px 48px rgba(0, 0, 0, 0.16);
```

### Bordures

```css
/* Rayons de bordure */
--radius-sm: 0.375rem;   /* 6px */
--radius-md: 0.5rem;     /* 8px */
--radius-lg: 0.75rem;    /* 12px */
--radius-xl: 1rem;       /* 16px */
--radius-2xl: 1.5rem;    /* 24px */
--radius-full: 9999px;   /* Cercle complet */
```

### Transitions

```css
/* Durées et easing */
--transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
--transition-base: 300ms cubic-bezier(0.4, 0, 0.2, 1);
--transition-normal: 400ms cubic-bezier(0.4, 0, 0.2, 1);
--transition-slow: 500ms cubic-bezier(0.4, 0, 0.2, 1);
```

### Composants Principaux

#### Boutons

```css
.btn-primary {
    background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
    color: white;
    box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);
    transition: all var(--transition-base);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
}
```

#### Cards

```css
.card {
    background: white;
    border-radius: var(--radius-xl);
    box-shadow: var(--shadow-md);
    padding: var(--space-8);
    border: 1px solid var(--color-light-dark);
    transition: all var(--transition-base);
}

.card:hover {
    box-shadow: var(--shadow-xl);
    transform: translateY(-4px);
}
```

#### Inputs

```css
.form-input {
    padding: var(--space-4);
    border: 2px solid var(--color-light-dark);
    border-radius: var(--radius-lg);
    transition: all var(--transition-base);
}

.form-input:focus {
    border-color: var(--color-primary);
    box-shadow: 0 0 0 4px rgba(255, 107, 107, 0.1);
}
```

### Animations

```css
/* Fade In Up */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Fade In */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* Scale In */
@keyframes scaleIn {
    from {
        opacity: 0;
        transform: scale(0.9);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}
```

### Responsive Design

Le design utilise une approche mobile-first avec des breakpoints :

```css
/* Mobile First */
@media (min-width: 640px) { /* sm */ }
@media (min-width: 768px) { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }
```

**Grilles adaptatives** :
- Mobile : 1 colonne
- Tablet : 2 colonnes
- Desktop : 3-4 colonnes

---

## Sécurité

### Mesures de Sécurité Implémentées

#### 1. Authentification Django

Le projet utilise le système d'authentification intégré de Django :

- Hachage des mots de passe avec PBKDF2
- Gestion sécurisée des sessions
- Protection contre les attaques de session fixation
- Déconnexion automatique après inactivité

#### 2. Protection CSRF

Tous les formulaires incluent automatiquement un token CSRF :

```html
<form method="post">
    {% csrf_token %}
    <!-- Champs du formulaire -->
</form>
```

#### 3. Validation des Entrées

**Côté Client** :
- Validation HTML5 (required, pattern, type)
- Validation JavaScript personnalisée

**Côté Serveur** :
- Validation Django Forms
- Nettoyage des entrées
- Types de données stricts

#### 4. Protection contre les Injections SQL

Django ORM protège automatiquement contre les injections SQL :

```python
# Sécurisé (ORM)
logements = Logement.objects.filter(ville=ville)

# Jamais utilisé (vulnérable)
# cursor.execute(f"SELECT * FROM logement WHERE ville = '{ville}'")
```

#### 5. Décorateurs d'Authentification

Les vues du dashboard sont protégées :

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    # Seuls les utilisateurs authentifiés peuvent accéder
    pass
```

#### 6. Gestion des Permissions

Les utilisateurs non authentifiés sont redirigés vers la page de login :

```python
LOGIN_URL = '/dashboard/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
```

### Bonnes Pratiques de Sécurité

- Utilisation de HTTPS en production
- Configuration des cookies sécurisés (HttpOnly, Secure)
- Limitation des tentatives de connexion
- Validation des fichiers uploadés
- Sanitization des entrées utilisateur

---

## Tests

### Stratégie de Tests

Le projet inclut des tests unitaires et fonctionnels pour assurer la qualité du code.

### Types de Tests

#### 1. Tests de Modèles

Validation de la logique métier au niveau des modèles :

```python
class ReservationModelTest(TestCase):
    def test_calcul_montant_total(self):
        logement = Logement.objects.create(prix_par_nuit=50000)
        reservation = Reservation(
            logement=logement,
            date_arrivee=date(2024, 1, 1),
            date_depart=date(2024, 1, 4)
        )
        reservation.save()
        self.assertEqual(reservation.montant_total, 150000)
```

#### 2. Tests de Formulaires

Validation des formulaires et de leur logique :

```python
class ReservationFormTest(TestCase):
    def test_dates_valides(self):
        form = ReservationForm({
            'date_arrivee': '2024-01-01',
            'date_depart': '2024-01-04'
        })
        self.assertTrue(form.is_valid())
```

#### 3. Tests de Vues

Validation du comportement des vues :

```python
class ListingViewTest(TestCase):
    def test_page_listings(self):
        response = self.client.get(reverse('listings'))
        self.assertEqual(response.status_code, 200)
```

### Exécution des Tests

```bash
# Tous les tests
python manage.py test

# Tests d'une application spécifique
python manage.py test principale
python manage.py test dashboard

# Tests avec verbosité
python manage.py test --verbosity=2

# Tests avec couverture
coverage run --source='.' manage.py test
coverage report
```

### Base de Données de Test

Les tests utilisent automatiquement SQLite pour isoler les tests de la base de données de production, garantissant que les tests ne modifient pas les données réelles.

---

## Déploiement

### Configuration de Production

#### 1. Variables d'Environnement

```bash
# .env
DEBUG=False
SECRET_KEY=votre_cle_secrete
DATABASE_URL=mysql://user:password@host:port/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

#### 2. Configuration Django

```python
# config/settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Base de données PostgreSQL en production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

# Fichiers statiques
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

#### 3. Collecte des Fichiers Statiques

```bash
python manage.py collectstatic --noinput
```

#### 4. Serveur de Production

Utilisation de Gunicorn avec Nginx :

```bash
# Installation de Gunicorn
pip install gunicorn

# Lancement de Gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

#### 5. Configuration Nginx

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /path/to/staticfiles/;
    }

    location /media/ {
        alias /path/to/media/;
    }
}
```

### Plateformes de Déploiement Suggérées

- **Heroku** : Simple pour les petits projets
- **DigitalOcean** : Plus de contrôle, bon rapport qualité-prix
- **AWS** : Pour les projets à grande échelle
- **Railway** : Moderne, facile à utiliser

---

## Conclusion

### Résumé du Projet

Gestion Immo est une application web complète de gestion de locations immobilières qui répond aux objectifs initiaux :

✅ Catalogue de logements avec recherche et filtrage
✅ Système de réservation en ligne avec validation
✅ Tableau de bord administratif fonctionnel
✅ Interface moderne et responsive
✅ Tests unitaires et fonctionnels
✅ Sécurité implémentée

### Points Forts

1. **Architecture Solide** : Séparation claire entre frontend et backend
2. **Design Moderne** : UI/UX soigné avec design system cohérent
3. **Sécurité** : Mesures de sécurité implémentées
4. **Extensibilité** : Code modulaire et maintenable
5. **Tests** : Couverture de tests pour la qualité

### Améliorations Possibles

1. **Intégration Paiement** : Stripe ou PayPal pour les paiements réels
2. **Notifications** : Emails pour les confirmations de réservation
3. **Reviews** : Système d'avis et de notes
4. **Carte Interactive** : Intégration Google Maps
5. **API REST** : Pour application mobile
6. **Messagerie** : Communication entre propriétaires et locataires

### Apprentissages

Ce projet a permis d'approfondir :
- Le framework Django et son pattern MVT
- La conception de bases de données relationnelles
- Le design system et l'UI/UX moderne
- La sécurité web et les bonnes pratiques
- Les tests et l'assurance qualité
- Le déploiement d'applications web

### Perspectives

Gestion Immo constitue une base solide pour une plateforme de location immobilière complète. Avec les améliorations suggérées, il pourrait évoluer vers un produit commercial viable.

---

## Annexes

### Ressources Utilisées

- **Documentation Django** : https://docs.djangoproject.com/
- **Lucide Icons** : https://lucide.dev/
- **Google Fonts** : https://fonts.google.com/
- **MDN Web Docs** : https://developer.mozilla.org/

### Screenshots

*(Ajouter des captures d'écran du projet ici)*

### Contact

Pour toute question sur ce projet, n'hésitez pas à contacter l'équipe de développement.

---

**Document version 1.0 - Juin 2026**
