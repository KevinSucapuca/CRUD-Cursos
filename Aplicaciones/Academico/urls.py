from django.urls import path
from . import views
urlpatterns = [
path('',views.home),
path('contacto/',views.contacto),
path('registrarCurso/',views.registrarCurso),
path('editarCurso/<codigo>',views.edicionCurso),
path('editarCurso/',views.editarCurso),
path('eliminarCurso/<codigo>',views.eliminarCurso),


]