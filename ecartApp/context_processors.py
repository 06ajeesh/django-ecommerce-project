from ecartApp.models import Cart,Order


def cart_and_order_count(request):
	if request.user.is_authenticated:
		cart_count = Cart.objects.filter(user=request.user, status='in-cart').count()
		order_count = Order.objects.filter(user=request.user).exclude(status='cancelled').count()
	else:
		cart_count = 0
		order_count = 0
	return {'cart_count': cart_count,'order_count': order_count}
