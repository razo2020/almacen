from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from inventory_management.settings import LOW_QUANTITY
from django.contrib import messages

class Index(TemplateView):
	template_name = 'inventory/index.html'

class Dashboard(LoginRequiredMixin, View):
	def get(self, request):
		items = Kardex.objects.filter(estado=True).order_by('id')

		return render(request, 'inventory/kardex.html', {'items': items})

class Invetario(LoginRequiredMixin, View):
	def get(self, request):
		items = Inventario.objects.all().order_by("id")
  				#filter(user=self.request.user.id).order_by('id')
		low_inventory_ids = Inventario.objects.filter(
			#user=self.request.user.id,
			stock__lte=LOW_QUANTITY
		).values_list('id', flat=True)

		if low_inventory_ids.count() > 0:
			if low_inventory_ids.count() > 1:
				messages.error(request, f'{low_inventory_ids.count()} items have low inventory')
			else:
				messages.error(request, f'{low_inventory_ids.count()} item has low inventory')

		return render(request, 'inventory/inventario.html', {'items': items, 'low_inventory_ids': low_inventory_ids})

	def post(self, request, *args, **kwargs):
		data = {}
		action = request.POST['action']
		try:
			if action == 'actualizar_inventario':
				kardexs = Kardex.objects.all()
				
			else:
				data['error'] = 'No ha seleccionado ninguna opción'
		except Exception as e:
			data['error'] = str(e)
   
		return HttpResponse(json.dumps(data), content_type='application/json')

class SignUpView(View):
	def get(self, request):
		form = UserRegisterForm()
		return render(request, 'inventory/signup.html', {'form': form})

	def post(self, request):
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			form.save()
			user = authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1']
			)

			login(request, user)
			return redirect('index')

		return render(request, 'inventory/signup.html', {'form': form})

class AddKardex(LoginRequiredMixin, CreateView):
	model = Kardex
	form_class = kardexForm
	template_name = 'inventory/kardex_form.html'
	success_url = reverse_lazy('kardex')
	titulo = "Kardex"
	#def get_context_data(self, **kwargs):
		#context = super().get_context_data(**kwargs)
		#context['categories'] = Category.objects.all()
		#return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EditKardex(LoginRequiredMixin, UpdateView):
	model = Kardex
	form_class = kardexForm
	template_name = 'inventory/kardex_form.html'
	success_url = reverse_lazy('kardex')
 
class ReporteMateriales(LoginRequiredMixin, View):
	def get(self, request):
		items = Material.objects.filter(estado=True).order_by('cod_material')

		return render(request, 'inventory/materiales.html', {'items': items})
 
class AddMaterial(LoginRequiredMixin, CreateView):
	model = Material
	form_class = MaterialForm
	template_name = 'inventory/material_form.html'
	success_url = reverse_lazy('materiales')
 
class EditMaterial(LoginRequiredMixin, UpdateView):
	model = Material
	form_class = MaterialForm
	template_name = 'inventory/material_form.html'
	success_url = reverse_lazy('materiales')

class DeleteItem(LoginRequiredMixin, DeleteView):
	model = InventoryItem
	template_name = 'inventory/delete_item.html'
	success_url = reverse_lazy('kardex')
	context_object_name = 'item'
