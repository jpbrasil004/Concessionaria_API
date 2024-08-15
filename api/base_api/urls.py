from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    path('modelos/', views.lista_modelos),
    path('modelos/<str:nome>/', views.modelo_unico),
    path('montadoras/', views.lista_montadoras),
    path('montadoras/<str:nome>/', views.montadora_unica),
]