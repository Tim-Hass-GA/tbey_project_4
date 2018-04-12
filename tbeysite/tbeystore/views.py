from django.shortcuts import render, redirect, get_object_or_404
from .models import Vendor, Question, Choice, Product, Category, Product_Order, Order
from .forms import LoginForm, SignUpForm, ProductForm, VendorForm, ProductOrderForm, AddToCartForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.decorators.http import require_POST
from .cart import Cart
from django.template import loader
import requests

# Create your views here.

####### TODO's #######
## TODO: refactor from def to class where necessary
# class IndexView(generic.ListView):
#     template_name = 'tbeystore/index.html'
#     context_object_name =
#     def get_queryset(self):
        # Return the last 5 published questions
        # not including those set for future publishing date
        # return Question.objects.filter(
        #     pub_date__lte=timezone.now()
        # ).order_by('-pub_date')[:5]
        # return Question.objects.filter(
        #     pub_date__lte=timezone.now()
        # ).order_by('-pub_date')[:5]
        # return Question.objects.order_by('-pub_date')[:5]

########## TODO: also -- refactor
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question':question})

##### GET HOME ROUTE
def index(request):
    vendors = Vendor.objects.all()
    products = Product.objects.all()
    # products = Product.objects.all()
    return render(request, 'tbeystore/index.html', {'vendors':vendors, 'products':products})

##### SHOW PRODUCT ROUTE
def product(request, product_id):
    product = Product.objects.get(id=product_id)
    questions = Question.objects.filter(product_id=product_id)
    # question_form = QuestionForm()
    cart_product_form = AddToCartForm()
    ## TODO: add api call for vendor such as EBAY --- COSTCO
#     # payload = {'key':'TOKEN'}
#     res = requests.get('http://thecatapi.com/api/images/get')
#     # res = requests.get('http://thecatapi.com/api/images/get', params=payload)
#     # return render(request, 'api.html', {'imageurl':res.url})
    return render(request, 'tbeystore/product.html', {
                    'product':product,
                    'questions':questions,
                    # 'question_form':question_form,
                    'cart_product_form':cart_product_form})


##### CREATE PRODUCT ROUTE
def post_product(request, vendor_id):
    print('posting product')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        vendor = Vendor.objects.get(pk=vendor_id)
        # method on the form object
        print(vendor)
        if form.is_valid():
            print('form valid')
            product = form.save(commit = False)
            product.vendor_id = int(vendor.id)
            print(product.vendor_id)
            product.save()
            print('saved')
            # return HttpResponseRedirect('/')
            return HttpResponseRedirect(reverse('tbeystore:vendor', args=(vendor.id,)))
        else:
            form = ProductForm()
            return render(request, 'tbeystore/vendor.html', {
                'form':form,
                'error_message': "Form is not valid."
            })
    else:
        form = LoginForm()
        return render(request, 'tbeystore/login.html', {
            'form':form,
            'error_message': "Something when wrong. Make sure you're signed in."
        })

##### PRODUCT PUT ROUTE
def edit_product(request, product_id):
    instance = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('tbeystore:product', args=(product_id,)))
            return HttpResponseRedirect(reverse('tbeystore:vendor', args=(instance.vendor_id,)))
    else:
        return render(request, 'tbeystore/edit_product.html', {'product':instance, 'form':form})

##### LIKE PRODUCT ROUTE
## TODO: add conditional for users ...............
def like_product(request):
    product_id = request.GET.get('product_id', None)
    likes = 0
    if (product_id):
        product = Product.objects.get(id=int(product_id))
        if product is not None:
            likes = product.likes + 1
            product.likes = likes
            product.save()
    return HttpResponse(likes)

##### PRODUCT DELETE ROUTE
def delete_product(request, product_id):
    if request.method == 'POST':
        instance = Product.objects.get(pk=product_id)
        instance.delete()
        return HttpResponseRedirect(reverse('tbeystore:vendor', args=(instance.vendor_id,)))


##### CREATE PRODUCT ORDER ROUTE
# class CreateOrderView(generic.ListView):
#     model = Order
#     template_name = 'tbeystore/order.html'
#
#     def get_queryset(self):
#         return Order.objects.filter()

def add_to_order(request, product_id, user_id):
    user = get_object_or_404(User, pk=user_id)
    print(user,'in add_to_order....')
    try:
        # selected_choice = Product.get(pk=request.POST['product'])
        product_item = get_object_or_404(Product, pk=product_id)
        print(product_item)
        if product_item.item_count != 0 or product_item.available:
            #  if the item is available and count is greater than 1
            #  create an instance of the Product Order to temporarily save order
            order_product = Product_Order()
            # associate order_product to user and product
            order_product.product = product_item
            order_product.product_count = 1
            order_product.product_price = product_item.price
            order_product.user = user
            order_product.payment = 'payment system not in place'
            if order_product.product is not None:
                print('saving order_product...')
                # reduce products inventory
                # save back into products
                if product_item.item_count != 0:
                    product_item.item_count -= 1
                product_item.save()
                order_product.save()
                # return HttpResponseRedirect(reverse, 'tbeystore:product', args=(product_item))
                return render(request, 'tbeystore/product.html', {
                    'product': product_item,
                    'error_message': "Order Saved."
                })
            else:
                return render(request, 'tbeystore/product.html', {
                    'product': product_item,
                    'error_message': "Something when wrong in your order."
                })
        else:
            # print(error)
            return render(request, 'tbeystore/product.html', {
                'product': product_item,
                'error_message': "Product is not available."
            })
    except (KeyError, Product.DoesNotExist):
        # redisplay the product
        return render(request, 'tbeystore/product.html', {
            'product': product_item,
            'error_message': "This item doesn't exist."
        })
    else:
        print('hit else add_to_order')
        # always return an HttpResponseRedirect after successfull POSTing data
        return HttpResponseRedirect(reverse('tbeystore:product', args=(product_item,)))


##### SHOPPING CART ROUTE
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        # print('cart_add form valid')
        cd = form.cleaned_data
        cart.add(product=product,
                    quantity=cd['quantity'],
                    update_quantity=cd['update'])
        print('calling cart details')
        return redirect('tbeystore:cart_detail')

# @require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    return redirect('tbeystore:cart_detail')

# @require_POST
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        print(item)
        item['update_quantity_form'] = AddToCartForm(initial = {'quantity':item['quantity'],
                                                        'update':True})
    return render(request, 'tbeystore/cart_detail.html', {'cart':cart})


#### VENDOR ####
##### VENDOR PROFILE ROUTE
def vendor(request, vendor_id):
    vendor = Vendor.objects.get(id=vendor_id)
    products = Product.objects.filter(vendor=vendor)
    # questions = Questions.objects.filter(products=products)
    form = ProductForm()
    return render(request, 'tbeystore/vendor.html', {'vendor':vendor, 'products':products, 'form':form})

##### VENDOR SIGN UP ROUTE
def vendor_signup(request, user_id):
    if request.method == 'POST':
        print('posting')
        user = User.objects.get(pk=user_id)
        form = VendorForm(request.POST)
        print(user)
        # print(user.id)
        if user is not None:
            if user.is_active:
                if form.is_valid():
                    print('form is valid')
                    # clean form
                    vendor = form.save(commit = False)
                    vendor.user_id = request.user.id
                    print(vendor.user_id)
                    vendor.save()
                    print('saved')
                    return HttpResponseRedirect('/')
                else:
                    print('from is not valid')
                    form = VendorForm()
                    return render(request, 'tbeystore/vendor_signup.html', {'form':form})
            else:
                form = LoginForm()
                return render(request, 'tbeystore/login.html', {
                    'form':form,
                    'error_message': "You must log in to create a vendor account."
                })
    else:
        form = VendorForm()
        return render(request, 'tbeystore/vendor_signup.html', {'form':form})


##### VENDOR PUT ROUTE
def edit_vendor(request, vendor_id):
    instance = get_object_or_404(Vendor, id=vendor_id)
    form = VendorForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tbeystore:vendor', args=(vendor_id,)))
    return render(request, 'tbeystore/edit_vendor.html', {'vendor':instance, 'form':form})

##### VENDOR DELETE ROUTE
def delete_vendor(request, vendor_id):
    if request.method == 'POST':
        instance = Vendor.objects.get(pk=vendor_id)
        instance.delete()
        return redirect('/')

#### USER PROFILE ROUTE
def profile(request, user_name):
    user = User.objects.get(username=user_name)
    # vendor = Vendor.objects.filter(user=user)
    return render(request, 'tbeystore/profile.html', {'username':user_name})

##### LOGIN ROUTE
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    print("This account has been disabled.")
                    return render(request, 'tbeystore/signup.html', {
                        'form':form,
                        'error_message': "This account has been disabled."
                    })
            else:
                print("The username and or password is incorrect.")
                # redisplay the login form
                return render(request, 'tbeystore/login.html', {
                    'form':form,
                    'error_message': "The username and or password is incorrect."
                })
    else:
        form = LoginForm()
        return render(request, 'tbeystore/login.html', {'form':form})

##### LOG OUT ROUTE
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

##### SIGN UP ROUTE
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            print("Something when wrong in the sign up process.")
            # redisplay the signup form
            return render(request, 'tbeystore/signup.html', {
                'form':form,
                'error_message':
                "Something when wrong in the sign up process. Please try again"
            })
    else:
        form = SignUpForm()
        return render(request, 'tbeystore/signup.html', {'form':form})


############ TODO: add these routes
##### _COMMENTS and _QUESTION ROUTE
class CommentsIndexView(generic.ListView):
    template_name = 'tbeystore/comments.html'
    context_object_name = 'Product'

    def get_queryset(self):
        # comments on products
        return HttpResponse("i need to be created")

    # TODO: add this to comments once in place
    def post_comment(request, new_comment):
        if request.session.get('has_commented', False):
            return HttpResponse("You've already commented.")
        c = comments.Comment(comment=new_comment)
        c.save()
        request.session['has_commented'] = True
        return HttpResponse('Thanks for your comment!')

############ TODO: Questions for users and vendors
## users about products
## vendors about user needs
class QuestionIndexView(generic.ListView):
    template_name = 'tbeystore/product.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # Return questions about products
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

##### _QUESTION DETAIL ROUTE
class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'tbeystore/question_detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

##### _QUESTION RESULTS ROUTE
class QuestionResultsView(generic.DetailView):
    model = Question
    template_name = 'tbeystore/question_results.html'

##### _QUESTION VOTE ROUTE
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'tbeystore/question_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # always return an HttpResponseRedirect after successfull POSTing data
        return HttpResponseRedirect(reverse('tbeystore:question_results', args=(question_id,)))

### API ROUTE
# requests is a thing....for api calls
def api(request):
    # payload = {'key':'TOKEN'}
    res = requests.get('http://thecatapi.com/api/images/get')
    # res = requests.get('http://thecatapi.com/api/images/get', params=payload)
    return render(request, 'tbeystore/adverts.html', {'imageurl':res.url})
