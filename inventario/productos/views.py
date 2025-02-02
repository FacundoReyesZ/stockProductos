from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Producto

# Create your views here.

# Vista para listar productos.

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/producto_list.html' # Nombre del template que se usará

# Vista para crear un nuevo producto

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'cantidad', 'precio'] # Campos a incluir en el formulario
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto_list') # Redirecciona a la lista de productos al guardar

# Vista para actualizar un producto existente

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'cantidad', 'precio']
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto_list')

# Vista para eliminar un producto

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')


