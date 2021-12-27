from django import forms


class OrderForm(forms.Form):
    addressId =  forms.ChoiceField(widget=forms.Select)