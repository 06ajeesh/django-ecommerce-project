from django.urls import path
from adminapp.views import AdminHome,AdminOrderView,AdminOrderUpdateView

urlpatterns = [
    path('', AdminHome.as_view(), name='admin_home'),
    path('order_list/', AdminOrderView.as_view(), name='admin_orders_list'),
    path('order_update/', AdminOrderUpdateView.as_view(), name='admin_orders_update'),
]