from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from ecartApp.models import Order
from adminapp.forms import OrderUpdateForm

# Create your views here.


class AdminHome(TemplateView):
    template_name = 'admin/admin_home.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['orders_count']=Order.objects.filter(status='order-placed').count()
        return context
    
    
class AdminOrderView(TemplateView):
    template_name = 'admin/order_list.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['orders']=Order.objects.all()
        return context
    
    
class AdminOrderUpdateView(FormView):
    template_name = 'admin/order_update.html'
    form_class = OrderUpdateForm