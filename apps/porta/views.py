from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Proyecto
# Create your views here.


class ProductoListView(generic.ListView):
    model = Proyecto
    template_name = "lista_proyecto.html"


class ProductoDetailView(generic.DetailView):
    model = Proyecto
    template_name = "detalle_proyecto.html"