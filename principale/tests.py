from datetime import date, timedelta
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .forms import ReservationRequestForm
from .models import Client, Logement, Reservation


class ReservationRequestFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {
            'logement_id': 1,
            'nom': 'Jean Dupont',
            'email': 'jean@example.com',
            'telephone': '+224 621 123 456',
            'date_arrivee': '2026-06-10',
            'date_depart': '2026-06-15',
            'card_number': '4242 4242 4242 4242',
            'card_expiry': '12/30',
            'card_cvc': '123',
        }
        form = ReservationRequestForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_card_number(self):
        form = ReservationRequestForm(data={
            'logement_id': 1,
            'nom': 'Jean Dupont',
            'email': 'jean@example.com',
            'telephone': '+224 621 123 456',
            'date_arrivee': '2026-06-10',
            'date_depart': '2026-06-15',
            'card_number': 'abcd 1234',
            'card_expiry': '12/30',
            'card_cvc': '123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('card_number', form.errors)

    def test_invalid_expiry_format(self):
        form = ReservationRequestForm(data={
            'logement_id': 1,
            'nom': 'Jean Dupont',
            'email': 'jean@example.com',
            'telephone': '+224 621 123 456',
            'date_arrivee': '2026-06-10',
            'date_depart': '2026-06-15',
            'card_number': '4242 4242 4242 4242',
            'card_expiry': '1230',
            'card_cvc': '123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('card_expiry', form.errors)

    def test_invalid_cvc(self):
        form = ReservationRequestForm(data={
            'logement_id': 1,
            'nom': 'Jean Dupont',
            'email': 'jean@example.com',
            'telephone': '+224 621 123 456',
            'date_arrivee': '2026-06-10',
            'date_depart': '2026-06-15',
            'card_number': '4242 4242 4242 4242',
            'card_expiry': '12/30',
            'card_cvc': '12',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('card_cvc', form.errors)

    def test_invalid_date_order(self):
        form = ReservationRequestForm(data={
            'logement_id': 1,
            'nom': 'Jean Dupont',
            'email': 'jean@example.com',
            'telephone': '+224 621 123 456',
            'date_arrivee': '2026-06-15',
            'date_depart': '2026-06-10',
            'card_number': '4242 4242 4242 4242',
            'card_expiry': '12/30',
            'card_cvc': '123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)


class ReservationModelTest(TestCase):
    def setUp(self):
        self.logement = Logement.objects.create(
            titre='Test Logement',
            description='Description test',
            adresse='Rue de Test',
            ville='Conakry',
            prix_par_nuit=Decimal('50000.00'),
            disponible=True,
        )
        self.client_obj = Client.objects.create(
            nom='Client Test',
            email='client@test.com',
            telephone='+224 621 000 000',
        )

    def test_save_calculates_montant_total(self):
        reservation = Reservation.objects.create(
            client=self.client_obj,
            logement=self.logement,
            date_arrivee=date(2026, 6, 10),
            date_depart=date(2026, 6, 15),
            statut='EN_ATTENTE',
        )
        self.assertEqual(reservation.montant_total, self.logement.prix_par_nuit * 5)

    def test_clean_rejects_departure_before_arrival(self):
        reservation = Reservation(
            client=self.client_obj,
            logement=self.logement,
            date_arrivee=date(2026, 6, 15),
            date_depart=date(2026, 6, 10),
            statut='EN_ATTENTE',
        )
        with self.assertRaises(Exception):
            reservation.full_clean()

    def test_clean_rejects_overlapping_confirmed_reservations(self):
        Reservation.objects.create(
            client=self.client_obj,
            logement=self.logement,
            date_arrivee=date(2026, 6, 10),
            date_depart=date(2026, 6, 15),
            statut='CONFIRMEE',
        )
        second_reservation = Reservation(
            client=self.client_obj,
            logement=self.logement,
            date_arrivee=date(2026, 6, 14),
            date_depart=date(2026, 6, 18),
            statut='EN_ATTENTE',
        )
        with self.assertRaises(Exception):
            second_reservation.full_clean()


class SiteViewTest(TestCase):
    def setUp(self):
        self.logement = Logement.objects.create(
            titre='Test Logement',
            description='Description test',
            adresse='Rue de Test',
            ville='Conakry',
            prix_par_nuit='40000.00',
            disponible=True,
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_listings_page_status_code(self):
        response = self.client.get(reverse('listings'))
        self.assertEqual(response.status_code, 200)

    def test_listing_detail_page_status_code(self):
        response = self.client.get(reverse('listing_detail', kwargs={'listing_id': self.logement.id}))
        self.assertEqual(response.status_code, 200)

    def test_reservation_page_loads(self):
        response = self.client.get(f"{reverse('reservation')}?listing_id={self.logement.id}")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Finaliser votre réservation')

    def test_contact_page_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
