# Gestion Immo

Application Django de gestion de location immobilière avec catalogue, réservation et interface d'administration.

## Description

Ce projet permet de consulter des logements, créer des demandes de réservation, puis gérer les réservations et les logements via un tableau de bord sécurisé.

## Installation

### Prérequis

- Python 3.13
- MySQL (ou PostgreSQL/SQLite pour développement)
- `pip`

### Installation des dépendances

1. Activez votre environnement virtuel ou utilisez Python global.
2. Installez les dépendances :

```bash
python -m pip install -r requirements.txt
```

### Configuration

Le projet utilise MySQL par défaut dans `config/settings.py` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gestion_immo',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

Si vous ne souhaitez pas utiliser MySQL, vous pouvez basculer sur SQLite en décommentant le bloc `sqlite3` présent dans le fichier de configuration.

### Initialisation de la base de données

1. Créez la base de données MySQL `gestion_immo`.
2. Appliquez les migrations :

```bash
python manage.py migrate
```

3. Créez un superutilisateur pour l'administration :

```bash
python manage.py createsuperuser
```

## Lancement

Pour démarrer le serveur local :

```bash
python manage.py runserver
```

Ensuite, ouvrez `http://127.0.0.1:8000/` dans votre navigateur.

## Tests

Le projet dispose maintenant de tests unitaires et fonctionnels pour les formulaires, les modèles et les vues principales.

Les tests utilisent SQLite automatiquement lorsque la commande `manage.py test` est lancée, afin d’isoler la suite des dépendances MySQL de production.

Pour exécuter les tests :

```bash
python manage.py test
```

## Points de validation et vérifications réalisées

- Formulaire de réservation : validation des dates, du numéro de carte, de l'expiration et du CVC.
- Modèle `Reservation` : calcul du montant total, vérification des dates et détection des chevauchements de réservations confirmées.
- Pages publiques : accueil, liste des logements, détail d'un logement, réservation et contact.
- Dashboard : page de connexion, redirection des utilisateurs non authentifiés, accès aux réservations après connexion.

## Bugs / améliorations identifiés

- La page `contact` contient un formulaire HTML statique qui n'est pas encore traité côté serveur.
- Le résumé de réservation côté client affiche des frais fixes (`25 000 GNF` et `15 000 GNF`) alors que le backend ne les ajoute pas automatiquement au montant total.
- Le panneau d'administration de création/modification de logement ne valide pas encore les champs de saisie (`prix_par_nuit`, `titre`, `ville`, etc.).
- Le formulaire de carte ne vérifie pas encore que la date d'expiration n'est pas passée.

## Structure du projet

- `principale/` : application front-office, modèles, formulaires, vues et templates.
- `dashboard/` : application back-office pour gérer logements et réservations.
- `config/` : configuration Django, URL routing et déploiement.

## Notes

- `requirements.txt` a été converti en UTF-8 pour garantir une installation sans problème.
- Le projet a passé la vérification `python manage.py check` sans erreurs.
