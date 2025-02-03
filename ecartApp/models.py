from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
	category = models.CharField(max_length=100)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.category


class Product(models.Model):
	product_name = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.PositiveIntegerField()
	image = models.ImageField(upload_to='images')
	description = models.TextField(max_length=250)

	def __str__(self):
		return self.product_name


class Cart(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	options = [
		('in-cart', 'in-cart'),
		('order-placed', 'order-placed'),
		('cancelled', 'cancelled'),
	]
	status = models.CharField(max_length=100, choices=options, default='in-cart')


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Cart, on_delete=models.CASCADE)
	address = models.TextField(max_length=250)
	phone = models.PositiveBigIntegerField(default=1234657890)
	options = [
		('order-placed', 'order-placed'),
		('cancelled', 'cancelled'),
		('delivered', 'delivered'),
		('dispatched', 'dispatched'),
		('out-for-delivery', 'out-for-delivery'),
	]
	status = models.CharField(max_length=100, choices=options, default='order-placed')
	created_at = models.DateTimeField(auto_now_add=True)