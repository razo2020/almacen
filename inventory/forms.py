from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class InventoryItemForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)
	class Meta:
		model = InventoryItem
		fields = ['name', 'quantity', 'category']
        
class kardexForm(forms.ModelForm):
    
    almacen = forms.ModelChoiceField(queryset=Almacen.objects.all(), initial=0)
    material = forms.ModelChoiceField(queryset=Material.objects.all(), initial=0)
    
    class Meta:
        model = Kardex
        fields = ['almacen', 'nom_ubicacion', 'material', 'movimiento', 'cantidad', 'orden_compra', 'guia', 'observacion']


class MaterialForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), initial=0)
    class Meta:
        model = Material
        fields = ['cod_material','nombre_material', 'descripcion_material', 'umb', 'categoria']
        
        