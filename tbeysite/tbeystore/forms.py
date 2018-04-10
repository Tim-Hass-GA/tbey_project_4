from django import forms
from .models import Vendor, Question, Product, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelChoiceField
# special extention

class VendorForm(forms.ModelForm):
    # user = forms.ModelChoiceField(queryset=User.objects.get(id=user_id))
    class Meta:
        model = Vendor
        fields = ('user','vendor_name','description','address','city','state','zip','website','email','phone',)


class ProductForm(forms.ModelForm):
    # category = forms.ModelChoiceField(queryset=Category.objects.all())
    # vendor_id = forms.ModelChoiceField(queryset=Vendor.objects.get(id=vendor_id))
    class Meta:
        model = Product
        fields = ('name','description','price','item_count','category', 'vendor')

        # widget = { 'category' : category}

# class ToyForm(forms.ModelForm):
#     class Meta:
#         model = Toy
#         fields = ('name',)

# Creating a form to change an existing article.
# >>> article = Article.objects.get(pk=1)
# >>> form = ArticleForm(instance=article)

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
