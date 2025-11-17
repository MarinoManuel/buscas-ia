from django.urls import path
from . import views


urlpatterns = [
    path('', views.BuscaView.as_view(), name='home'),
    path('buscar', views.BuscaView.as_view(), name='buscar'),
]
