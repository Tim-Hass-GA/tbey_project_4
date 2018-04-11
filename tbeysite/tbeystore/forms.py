from django import forms
from .models import Vendor, Question, Product, Category, Product_Order, Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelChoiceField
# special extention

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('vendor_name','description','address','city','state','zip','website','email','phone')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','description','price','item_count','category',)


class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = Product_Order
        fields = ('product', 'user', 'payment')
        # fields = ('product', 'vendor', 'product_count', 'order')

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=False)
    last_name = forms.CharField(max_length=30,required=False)
    email = forms.EmailField(max_length=254,help_text="Email is required")
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
