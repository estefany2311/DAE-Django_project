from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_citas, name='lista_citas'),
    path('crear/', views.crear_cita, name='crear_cita'),
    path('<int:cita_id>/estado/', views.actualizar_estado, name='actualizar_estado'),
    path('<int:cita_id>/eliminar/', views.eliminar_cita, name='eliminar_cita'),
    path('<int:cita_id>/', views.detalle_cita, name='detalle_cita'),
]