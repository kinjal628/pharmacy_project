from django import forms
from .models import Medicine, Supplier, Order

class MedicineForm(forms.ModelForm):
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    class Meta:
        model = Medicine
        fields = '__all__'

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['medicine', 'customer_name', 'quantity']
