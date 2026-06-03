from django import forms
from django.core.exceptions import ValidationError


class ReservationRequestForm(forms.Form):
    logement_id = forms.IntegerField(widget=forms.HiddenInput)
    nom = forms.CharField(
        max_length=100,
        label='Nom complet',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Votre nom complet', 'required': 'required'})
    )
    email = forms.EmailField(
        max_length=255,
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'votre@email.com', 'required': 'required'})
    )
    telephone = forms.CharField(
        max_length=20,
        label='Téléphone',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+224 XX XX XX XX', 'required': 'required'})
    )
    date_arrivee = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input', 'required': 'required'}),
        label='Date d\'arrivée'
    )
    date_depart = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input', 'required': 'required'}),
        label='Date de départ'
    )
    card_number = forms.CharField(
        max_length=19,
        label='Numéro de carte',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '0000 0000 0000 0000', 'required': 'required'})
    )
    card_expiry = forms.CharField(
        max_length=5,
        label='Expiration (MM/AA)',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'MM/AA', 'required': 'required'})
    )
    card_cvc = forms.CharField(
        max_length=4,
        label='CVC',
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': '123', 'required': 'required'})
    )

    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number', '').replace(' ', '')
        if not card_number.isdigit() or not 13 <= len(card_number) <= 19:
            raise ValidationError('Veuillez saisir un numéro de carte valide.')
        return card_number

    def clean_card_expiry(self):
        expiry = self.cleaned_data.get('card_expiry', '').strip()
        if not expiry:
            raise ValidationError('Veuillez indiquer la date d’expiration de la carte.')

        parts = expiry.split('/')
        if len(parts) != 2 or not all(part.isdigit() for part in parts):
            raise ValidationError('Format d’expiration invalide. Utilisez MM/AA.')

        month = int(parts[0])
        year = int(parts[1])
        if month < 1 or month > 12:
            raise ValidationError('Mois d’expiration invalide.')
        return expiry

    def clean_card_cvc(self):
        cvc = self.cleaned_data.get('card_cvc', '').strip()
        if not cvc.isdigit() or not 3 <= len(cvc) <= 4:
            raise ValidationError('Code de sécurité invalide.')
        return cvc

    def clean(self):
        cleaned_data = super().clean()
        arrivee = cleaned_data.get('date_arrivee')
        depart = cleaned_data.get('date_depart')

        if arrivee and depart and depart <= arrivee:
            raise ValidationError("La date de départ doit être après la date d'arrivée.")

        return cleaned_data
