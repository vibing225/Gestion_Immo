from django.contrib import admin
from .models import Logement, Client, Reservation, ImageLogement

admin.site.register(Logement)
admin.site.register(Client)
admin.site.register(Reservation)
admin.site.register(ImageLogement)