from datetime import date
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from principale.models import Logement, Reservation, Client


class DashboardViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='testpass')
        self.logement = Logement.objects.create(
            titre='Temp Logement',
            description='Test',
            adresse='Rue Test',
            ville='Conakry',
            prix_par_nuit=Decimal('35000.00'),
            disponible=True,
        )
        self.client_obj = Client.objects.create(
            nom='Client Test',
            email='client@test.com',
            telephone='+224 621 000 000',
        )
        self.reservation = Reservation.objects.create(
            client=self.client_obj,
            logement=self.logement,
            date_arrivee=date(2026, 6, 10),
            date_depart=date(2026, 6, 12),
            statut='EN_ATTENTE',
        )

    def test_login_page_accessible(self):
        response = self.client.get(reverse('dashboard:login'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_redirects_if_not_authenticated(self):
        response = self.client.get(reverse('dashboard:index'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('dashboard:login'), response.url)

    def test_login_with_valid_credentials(self):
        response = self.client.post(reverse('dashboard:login'), {
            'username': 'admin',
            'password': 'testpass',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('dashboard:index'))

    def test_reservations_page_requires_login(self):
        self.client.login(username='admin', password='testpass')
        response = self.client.get(reverse('dashboard:reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Réservation')
