from decimal import Decimal, InvalidOperation

from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ReservationRequestForm
from .models import Client, Logement, Reservation


def home(request):
    featured_listings = Logement.objects.filter(disponible=True)[:3]
    return render(request, 'principale/home.html', {'featured_listings': featured_listings})


def listings(request):
    search_query = request.GET.get('q', '').strip()
    ville = request.GET.get('ville', '').strip()
    min_price = request.GET.get('min_price', '').strip()
    max_price = request.GET.get('max_price', '').strip()

    all_listings = Logement.objects.filter(disponible=True)

    if search_query:
        all_listings = all_listings.filter(
            Q(titre__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(ville__icontains=search_query) |
            Q(adresse__icontains=search_query)
        )

    if ville:
        all_listings = all_listings.filter(ville__icontains=ville)

    try:
        if min_price:
            all_listings = all_listings.filter(prix_par_nuit__gte=Decimal(min_price))
    except InvalidOperation:
        min_price = ''

    try:
        if max_price:
            all_listings = all_listings.filter(prix_par_nuit__lte=Decimal(max_price))
    except InvalidOperation:
        max_price = ''

    context = {
        'listings': all_listings,
        'search_query': search_query,
        'ville': ville,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'principale/listings.html', context)


def listing_detail(request, listing_id):
    listing = get_object_or_404(Logement, id=listing_id, disponible=True)
    return render(request, 'principale/listing_detail.html', {'listing': listing})


def reservation(request):
    listing_id = request.GET.get('listing_id') or request.POST.get('logement_id')
    listing = get_object_or_404(Logement, id=listing_id, disponible=True)

    if request.method == 'POST':
        form = ReservationRequestForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            telephone = form.cleaned_data['telephone']
            date_arrivee = form.cleaned_data['date_arrivee']
            date_depart = form.cleaned_data['date_depart']

            client, created = Client.objects.get_or_create(
                email=email,
                defaults={'nom': nom, 'telephone': telephone}
            )

            if not created:
                client.nom = nom
                client.telephone = telephone
                client.save()

            reservation = Reservation(
                client=client,
                logement=listing,
                date_arrivee=date_arrivee,
                date_depart=date_depart,
                statut='EN_ATTENTE'
            )

            try:
                reservation.full_clean()
                reservation.save()
                return redirect(f"{reverse('confirmation')}?reservation_id={reservation.id}")
            except ValidationError as exc:
                form.add_error(None, exc)
    else:
        initial_data = {'logement_id': listing.id}
        if request.GET.get('check_in'):
            initial_data['date_arrivee'] = request.GET.get('check_in')
        if request.GET.get('check_out'):
            initial_data['date_depart'] = request.GET.get('check_out')
        form = ReservationRequestForm(initial=initial_data)

    return render(request, 'principale/reservation.html', {
        'listing': listing,
        'form': form,
    })


def confirmation(request):
    reservation = None
    reservation_id = request.GET.get('reservation_id')
    if reservation_id:
        reservation = Reservation.objects.filter(id=reservation_id).first()

    return render(request, 'principale/confirmation.html', {
        'reservation': reservation,
    })


def about(request):
    return render(request, 'principale/about.html')


def contact(request):
    return render(request, 'principale/contact.html')
