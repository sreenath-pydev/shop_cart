from django import forms
from django.contrib.auth.models import User
from .models import Product, CartItem, UserAddress

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    confirm_password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']

class CartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']

class AddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ['customer_name', 'place', 'phone', 'state', 'pincode']
