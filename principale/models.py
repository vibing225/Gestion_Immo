from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Logement(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)

    # Prix par nuitée (doit être positif)
    prix_par_nuit = models.DecimalField(max_digits=10, decimal_places=2)

    # Disponibilité globale du logement (hors réservations)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titre


class Client(models.Model):
    nom = models.CharField(max_length=100)

    # Email unique (important pour identifier un client)
    email = models.EmailField(unique=True)

    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom


class Reservation(models.Model):
    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'),
        ('CONFIRMEE', 'Confirmée'),
        ('REFUSEE', 'Refusée'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE)

    date_arrivee = models.DateField()
    date_depart = models.DateField()

    statut = models.CharField(
        max_length=50,
        choices=STATUT_CHOICES,
        default='EN_ATTENTE'
    )

    # Montant total figé au moment de la réservation (RG-05)
    montant_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    def clean(self):
        """
        VALIDATIONS MÉTIER (RG-03 et RG-04)
        """

        # RG-03 : date de départ doit être après date d'arrivée
        if self.date_depart <= self.date_arrivee:
            raise ValidationError("La date de départ doit être après la date d'arrivée.")

        # RG-04 : éviter les chevauchements de réservations confirmées
        if self.logement_id:
            conflits = Reservation.objects.filter(
                logement=self.logement,
                statut='CONFIRMEE'
            ).exclude(id=self.id)

            for r in conflits:
                if self.date_arrivee < r.date_depart and self.date_depart > r.date_arrivee:
                    raise ValidationError(
                        "Ce logement est déjà réservé sur cette période."
                    )

    def save(self, *args, **kwargs):
        """
        SURCHARGE SAVE :
        permet de calculer automatiquement le montant total (RG-05)
        """

        # Calcul du nombre de nuits
        if self.date_arrivee and self.date_depart:
            nb_nuits = (self.date_depart - self.date_arrivee).days

            # calcul du prix total basé sur le prix du logement
            if self.logement:
                self.montant_total = nb_nuits * self.logement.prix_par_nuit

        # Validation avant sauvegarde
        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.client} - {self.logement}"


class ImageLogement(models.Model):
    logement = models.ForeignKey(
        Logement,
        on_delete=models.CASCADE,
        related_name="images"
    )

    # Image stockée dans MEDIA/logements/
    image = models.ImageField(upload_to='logements/')

    def __str__(self):
        return f"Image de {self.logement}"