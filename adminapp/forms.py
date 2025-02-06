from django import forms

class OrderUpdateForm(forms.Form):
    product=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    quantity=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    user=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    options=(
        ('out-of-stock','out-of-stock'),
        ('order-placed', 'order-placed'),
		('cancelled', 'cancelled'),
		('delivered', 'delivered'),
		('dispatched', 'dispatched'),
		('out-for-delivery', 'out-for-delivery'),
    )
    status=forms.ChoiceField(choices=options,widget=forms.Select(attrs={'class':'form-control'}))
    expected_delivery_date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))