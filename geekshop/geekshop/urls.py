
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main),
    path('about/', mainapp.about),
    path('contact/', mainapp.contact),
    path('admin/', admin.site.urls),
]
