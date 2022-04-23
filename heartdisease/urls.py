import imp
from multiprocessing.spawn import import_main_path
from os import stat
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('heartapp.urls'))
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
