from django.contrib import admin
from .models import ImageLogement, Logement, Client, Reservation

admin.site.register(Logement)
admin.site.register(Client)
admin.site.register(Reservation)
admin.site.register(ImageLogement)
