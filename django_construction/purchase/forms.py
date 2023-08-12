from django import forms
from supplier.models import Supplier
from construction.models import Site
from .models import Purchase
from datetime import date
from django.forms import formset_factory

class PurchaseForm(forms.Form):
    site = forms.ModelChoiceField(label='Site Name', queryset=Site.objects.all(), widget=forms.Select(attrs={'class': 'form-control select'}))
    supplier = forms.ModelChoiceField(label='Supplier Name', queryset=Supplier.objects.all(), widget=forms.Select(attrs={'class': 'form-control select', 'id':'supplierId'}))
    invoice_no = forms.IntegerField(label='Invoice No', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Invoice No'}))
    purchase_date = forms.DateField(label='Invoice Date', widget=forms.DateInput(attrs={'class': 'form-control datepicker'}),
        initial=date.today(),)
    detail = forms.CharField(label='Note', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'cols': 8}))

    product = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    in_stock = forms.DecimalField(label='Stock', widget=forms.TextInput(attrs={'class': 'form-control'}), decimal_places=2, max_digits=10)
    qty = forms.DecimalField(label='Qty', widget=forms.TextInput(attrs={'class': 'form-control'}), decimal_places=2, max_digits=10)
    price = forms.DecimalField(label='Unit Price', widget=forms.TextInput(attrs={'class': 'form-control'}), decimal_places=2, max_digits=10)
    vat = forms.DecimalField(label='Unit VAT', widget=forms.TextInput(attrs={'class': 'form-control'}), decimal_places=2, max_digits=10)
    discount = forms.DecimalField(label='Unit Discount', widget=forms.TextInput(attrs={'class': 'form-control'}), decimal_places=2, max_digits=10)
    net_amount = forms.DecimalField(label='Net Amount', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}), decimal_places=2, max_digits=10)

    total_amount = forms.DecimalField(label='Total Amount', widget=forms.TextInput(attrs={'class': 'form-control netAmnt', 'readonly': True}), decimal_places=2, max_digits=10)
    total_vat = forms.DecimalField(label='Total Vat', widget=forms.TextInput(attrs={'class': 'form-control netVat', 'readonly': True}), decimal_places=2, max_digits=10)
    total_discount = forms.DecimalField(label='Total Discount', widget=forms.TextInput(attrs={'class': 'form-control netDis', 'readonly': True}), decimal_places=2, max_digits=10)
    net_payable = forms.DecimalField(label='Net Payable', widget=forms.TextInput(attrs={'class': 'form-control gtotal', 'readonly': True}), decimal_places=2, max_digits=10)
    paid_amount = forms.DecimalField(label='Total Paid', widget=forms.TextInput(attrs={'class': 'form-control paid'}), decimal_places=2, max_digits=10)
    total_due = forms.DecimalField(label='Total Due', widget=forms.TextInput(attrs={'class': 'form-control due', 'readonly': True}), decimal_places=2, max_digits=10)

    PAYMENT_CHOICES = (('', 'Select One'),('cash', 'Cash'),('card', 'Card'),('check', 'Check'),('bkash_nagad', 'Bkash/Nagad'))

    payment_type = forms.ChoiceField(label='Payment Type',choices=PAYMENT_CHOICES,widget=forms.Select(attrs={'class': 'form-control select'}))
    receiver_name = forms.CharField(label='Receiver Name', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Receiver Name'}))
    receiver_contact = forms.CharField(label='Receiver Contact', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Phone'}))
    issue_date = forms.DateField(label='Pay Date', widget=forms.DateInput(attrs={'class': 'form-control datepicker'}),
        initial=date.today(),)

    class Meta:
        model = Purchase
        fields = ['site', 'supplier', 'invoice_no', 'purchase_date', 'detail', 'total_amount', 'total_vat', 'total_discount', 'net_payable', 'user']
