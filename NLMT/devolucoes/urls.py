from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_devoluções, name='lista_devoluções'),
    path('nova_devolução/', views.nova_devolução, name='nova_devolução'),
    path('atualizar_status/', views.atualizar_status, name='atualizar_status'),
]
