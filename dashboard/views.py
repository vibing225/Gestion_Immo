from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from principale.models import Logement, Reservation, Client, ImageLogement


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard:index')
        messages.error(request, 'Identifiants incorrects.')
    return render(request, 'dashboard/login.html')


def logout_view(request):
    logout(request)
    return redirect('dashboard:login')


@login_required(login_url='/dashboard/login/')
def index(request):
    total_logements = Logement.objects.count()
    total_reservations = Reservation.objects.count()
    en_attente = Reservation.objects.filter(statut='EN_ATTENTE').count()
    confirmees = Reservation.objects.filter(statut='CONFIRMEE').count()
    annulees = Reservation.objects.filter(statut='REFUSEE').count()
    revenus = Reservation.objects.filter(statut='CONFIRMEE').aggregate(
        total=Sum('montant_total'))['total'] or 0
    dernieres = Reservation.objects.select_related('client', 'logement').order_by('-id')[:5]

    context = {
        'total_logements': total_logements,
        'total_reservations': total_reservations,
        'en_attente': en_attente,
        'confirmees': confirmees,
        'annulees': annulees,
        'revenus': revenus,
        'dernieres': dernieres,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='/dashboard/login/')
def logements(request):
    liste = Logement.objects.prefetch_related('images').all()
    return render(request, 'dashboard/logements.html', {'logements': liste})


@login_required(login_url='/dashboard/login/')
def logement_form(request, pk=None):
    logement = get_object_or_404(Logement, pk=pk) if pk else None
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        prix = request.POST.get('prix_par_nuit')
        disponible = request.POST.get('disponible') == 'on'

        if logement:
            logement.titre = titre
            logement.description = description
            logement.adresse = adresse
            logement.ville = ville
            logement.prix_par_nuit = prix
            logement.disponible = disponible
            logement.save()
            messages.success(request, 'Logement modifié avec succès.')
        else:
            logement = Logement.objects.create(
                titre=titre, description=description,
                adresse=adresse, ville=ville,
                prix_par_nuit=prix, disponible=disponible
            )
            messages.success(request, 'Logement ajouté avec succès.')

        # Gestion images
        for img in request.FILES.getlist('images'):
            ImageLogement.objects.create(logement=logement, image=img)

        return redirect('dashboard:logements')

    return render(request, 'dashboard/logement_form.html', {'logement': logement})


@login_required(login_url='/dashboard/login/')
def logement_supprimer(request, pk):
    logement = get_object_or_404(Logement, pk=pk)
    if request.method == 'POST':
        logement.delete()
        messages.success(request, 'Logement supprimé.')
    return redirect('dashboard:logements')


@login_required(login_url='/dashboard/login/')
def reservations(request):
    liste = Reservation.objects.select_related('client', 'logement').order_by('-id')
    return render(request, 'dashboard/reservations.html', {'reservations': liste})


@login_required(login_url='/dashboard/login/')
def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation.objects.select_related('client', 'logement'), pk=pk)
    return render(request, 'dashboard/reservation_detail.html', {'reservation': reservation})


@login_required(login_url='/dashboard/login/')
def reservation_confirmer(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.statut = 'CONFIRMEE'
    reservation.save()
    messages.success(request, 'Réservation confirmée.')
    return redirect('dashboard:reservations')


@login_required(login_url='/dashboard/login/')
def reservation_annuler(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.statut = 'REFUSEE'
    reservation.save()
    messages.success(request, 'Réservation annulée.')
    return redirect('dashboard:reservations')


@login_required(login_url='/dashboard/login/')
def reservation_supprimer(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Réservation supprimée.')
    return redirect('dashboard:reservations')


@login_required(login_url='/dashboard/login/')
def parametres(request):
    if request.method == 'POST':
        messages.success(request, 'Paramètres enregistrés.')
        return redirect('dashboard:parametres')
    return render(request, 'dashboard/parametres.html')
