from django.contrib import admin
from .models import Clients
from .models import Reservations
from .models import PlacesLibres
from .models import Abonnements

# Register your models here.

admin.site.register(Clients)
admin.site.register(Reservations)
admin.site.register(PlacesLibres)
admin.site.register(Abonnements)