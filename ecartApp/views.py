import datetime
from ecartApp.decorators import is_log_in
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from ecartApp.models import Product, Cart, Order
from ecartApp.forms import RegisterForm, LoginForm, CartForm, OrderForm
from django.views.generic import DetailView, CreateView, FormView, ListView, DeleteView
from django import views
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER


# Create your views here.

class WelcomeView(TemplateView):
	template_name = 'welcome.html'


class HomeView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['products'] = Product.objects.all()
		return context


class ProductView(DetailView):
	template_name = 'detail_product.html'
	pk_url_kwarg = 'id'
	model = Product
	context_object_name = 'product'


class RegisterView(CreateView):
	form_class = RegisterForm
	model = User
	template_name = 'registration_page.html'

	# success_url = reverse_lazy('home')

	def form_valid(self, form):
		User.objects.create_user(**form.cleaned_data)
		messages.success(self.request, 'Registration successful')
		return redirect('home')

	def form_invalid(self, form):
		messages.error(self.request, 'Invalid credentials')
		return super().form_invalid(form)


class LoginView(FormView):
	template_name = 'login_page.html'
	form_class = LoginForm

	def post(self, request, *args, **kwargs):
		uname = request.POST.get('username')
		psw = request.POST.get('password')
		user = authenticate(request, username=uname, password=psw)
		if user:
			login(request, user)
			print('success')
			if user.is_superuser == 1:
				messages.success(request, "Welcome Admin")
				return redirect('admin_home')
			else:
				messages.success(request, f"Login Success @{user.username}")
				return redirect('home')
		else:
			print('error')
			messages.warning(request, "Login Failed")
			return redirect('login_user')


class LogoutView(views.View):
	def get(self, request):
		if request.user.is_authenticated:
			logout(request)
			messages.success(request, 'Logout Success')
		else:
			messages.warning(request, "Please Login")
		return redirect('login_user')


@method_decorator(is_log_in, name='dispatch')
class CartView(views.View):
	def get(Self, request, *args, **kwargs):
		product = Product.objects.get(id=kwargs.get('id'))
		form = CartForm()
		return render(request, "add_cart.html", {'form': form, 'product': product})

	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			product = Product.objects.get(id=kwargs.get('id'))
			user = request.user
			quantity = request.POST.get('quantity')
			cart_content = Cart.objects.filter(product=product, user=user, status='in-cart')
			if cart_content:
				messages.success(request, 'Cart Updated')
				cart_content[0].quantity += int(quantity)
				cart_content[0].save()
			else:
				Cart.objects.create(product=product, user=user, quantity=quantity)
				messages.success(request, 'Product added to cart')
		else:
			messages.success(request, 'you need to login first 😁')
		return redirect('home')


@method_decorator(is_log_in, name='dispatch')
class CartListView(ListView):
	model = Cart
	template_name = 'cart_list.html'
	context_object_name = 'cart_list'

	def get_queryset(self):
		return Cart.objects.filter(user=self.request.user, status='in-cart')


@method_decorator(is_log_in, name='dispatch')	
class CartDeleteView(views.View):
	def post(self, request, *args, **kwargs):
		cart = Cart.objects.get(id=kwargs.get('id'))
		cart.delete()
		print('deleted')
		messages.success(request, 'Product removed from cart')
		return redirect('cart_list_view')

@method_decorator(is_log_in, name='dispatch')
class PlaceOrderView(TemplateView):
	template_name = 'place_order.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cart_id = kwargs.get('id', None)
		if cart_id:
			context['cart_list'] = Cart.objects.filter(id=cart_id, user=self.request.user, status='in-cart')
		else:
			context['cart_list'] = Cart.objects.filter(user=self.request.user, status='in-cart')
		context['form'] = OrderForm()
		return context

	def post(self, request, *args, **kwargs):
		cart = Cart.objects.get(id=kwargs.get('id'))
		user = request.user
		email = user.email
		address = request.POST.get('address')
		phone = request.POST.get('phone', None)
		print('order initialising')
		print(user, email, address, cart)
		Order.objects.create(user=user, product=cart, address=address)
		cart.status = "order-placed"
		cart.save()
		message = f'''Your order is successfully placed 
		
Address 		: {address}
Phone 			: {phone}
Product 		: {cart.product.product_name}
Quantity 		: {cart.quantity}
Order Time 		: {datetime.datetime.now()}
Description 	: {cart.product.description}

					
Thank you for the order !!! 
					'''
		to_addr = email
		confirmation = send_mail("Order confirmation", message, EMAIL_HOST_USER, [to_addr])
		print(confirmation)
		if confirmation == 1:
			messages.success(request, 'Product Order Success')
			return redirect('home')
		else:
			messages.warning(request, "Error occurred during order placement")
			return redirect('cart_list_view')

@method_decorator(is_log_in, name='dispatch')
class OrdersView(TemplateView):
	template_name = 'order_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		orders = Order.objects.filter(user=self.request.user).exclude(status='cancelled')
		print(orders)
		context['orders'] = orders
		return context

@method_decorator(is_log_in, name='dispatch')
class OrderCancelView(DeleteView):
	template_name = 'order_cancel.html'
	pk_url_kwarg = 'id'
	model = Order
	success_url = reverse_lazy('orders_list_view')

	def get_context_data(self, **kwargs):
		messages.success(self.request, 'Order Cancelling')
		context = super().get_context_data(**kwargs)
		return context

