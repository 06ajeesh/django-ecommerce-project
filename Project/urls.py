"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from ecartApp import views
from django.conf import settings
from django.conf.urls.static import static
from adminapp.views import AdminHome

urlpatterns = [
				  path('admin/', admin.site.urls),
				  path('admin-home', include('adminapp.urls')),
				  path('', views.WelcomeView.as_view(), name='welcome'),
				  path('login_user', views.LoginView.as_view(), name='login_user'),
				  path('logout_user', views.LogoutView.as_view(), name='logout_user'),
				  path('register_user/', views.RegisterView.as_view(),name='register_user'),
				  path('home/', views.HomeView.as_view(), name='home'),
				  path('cart/list', views.CartListView.as_view(), name='cart_list_view'),
				  path('orders/list', views.OrdersView.as_view(), name='orders_list_view'),
				  path('details/<int:id>', views.ProductView.as_view(),name='detail_view'),
				  path('add_to_cart/<int:id>', views.CartView.as_view(),name='add_to_cart_view'),
				  path('cart/delete/<int:id>', views.CartDeleteView.as_view(),name='cart_item_delete_view'),
				  path('cart/order/<int:id>', views.PlaceOrderView.as_view(),name='cart_item_order_view'),
      			  path('order/cancel/<int:id>', views.OrderCancelView.as_view(),name='order_item_cancel_view'),
			  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)