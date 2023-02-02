from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core import views 

#Inclusion de una direccion geneal para las url de la app core que se encuentran dentro del archivo urls.py
urlpatterns = [
     #app core
    path('', include('core.urls')),
    #admin
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)