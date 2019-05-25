
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$^', views.paginaInicial),
    url(r'^login/',views.paginaLogin),
    url(r'^registro', views.paginaRegistro),
]