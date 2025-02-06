from django.shortcuts import render,redirect
from django.views.generic import TemplateView,FormView
from ecartApp.models import Order,Product,Cart
from adminapp.forms import OrderUpdateForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib import messages
from django.db.models import Q

# Create your views here.


class AdminHome(TemplateView):
    template_name = 'admin/admin_home.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['orders_count']=Order.objects.exclude(Q(status='delivered') | Q(status='cancelled') ).count()
        return context
    
    
class AdminOrderView(TemplateView):
    template_name = 'admin/order_list.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['orders']=Order.objects.all()
        return context
    
    
class AdminOrderUpdateView(TemplateView):
    template_name = 'admin/order_update.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        o_id=kwargs.get('id')
        order=Order.objects.get(id=o_id)
        context['form']=OrderUpdateForm(initial= {'status':order.status,'product':order.product.product.product_name,'user':order.user,'quantity':order.product.quantity,'expected_delivery_date':'2021-06-01'})
        return context
    
    def post(self,request,*args,**kwargs):
        
        # getting data from form
        o_id=kwargs.get('id')
        order=Order.objects.get(id=o_id)
        quantity=request.POST.get('quantity')
        user = request.POST.get('user')
        status=request.POST.get('status')
        product=request.POST.get('product')
        expected_delivery_date=request.POST.get('expected_delivery_date')
        email=order.user.email
        
        #updating order
        order.product.quantity=quantity
        order.product.save()
        order.status=status
        order.save()
        
        # sending mail
        
        if status=='out-of-stock':
            message=f'''
Hello {user},

We are sorry to inform you that the product {product} is out of stock
'''
        elif status=='cancelled':
            message=f'''
Hello {user},

We are sorry to inform you that the product {product} is cancelled.
'''
        elif status=='delivered':
            message=f'''
Hello {user},

We are happy to inform you that the product {product} is delivered.
'''
        else:
                    message = f'''
        
Hello {user},
        
Your order is updated
Details : 
        Product: {product}
        Quantity: {quantity}
        Status: {status}
        Expected Delivery Date: {expected_delivery_date}
        
Thank you for shopping with us

'''

        confirmation = send_mail("Order Updation", message, EMAIL_HOST_USER, ['ajeeshperalayil@gmail.com'])
        print(confirmation)
        messages.success(request, 'Order updated successfully')
        return redirect('admin_home')