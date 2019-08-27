from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'
urlpatterns = [
    path('', mainapp.pricelist, name='index'),
    path('<int:pk>/', mainapp.pricelist, name='category'),
    ]