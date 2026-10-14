from django.contrib import admin
from django.urls import path,include
from django.urls import path
from Gestion_Parking import views

urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('Gestion_Parking.urls')),
         path('Registration',views.Registration,name='Registration'),
         path('Login',views.Login,name='Login'),
         path('Dashboard',views.Dashboard,name='Dashboard'),
]

