from django import forms
from django.contrib.auth.models import User
from ecartApp.models import Cart, Order


class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'username', 'email', 'password']
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control'}),
		}


class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control'}),
		}


class CartForm(forms.ModelForm):
	class Meta:
		model = Cart
		fields = ['quantity']
		widgets = {
			'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
		}


class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['address', 'phone']
		widgets = {
			'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': 'required'}),
			'phone': forms.NumberInput(attrs={'class': 'form-control'}),
		}