from django.shortcuts import render, redirect, get_object_or_404
from .models import Vendor, Question, Choice, Product, Category
from .forms import LoginForm, SignUpForm, ProductForm, VendorForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# from django.template import loader
import requests

# Create your views here.
#  “index” page – displays the home view.
#  “detail” page – displays a question text, with no results but with a form to vote.
#  “results” page – displays results for a particular item.
#  action – handles action for a particular choice in a particular question.
#  example template should be at polls/templates/polls/index.html

##### GET HOME ROUTE
def index(request):
    vendors = Vendor.objects.all()
    products = Product.objects.all()
    # form = CatForm()
    return render(request, 'tbeystore/index.html', {'vendors':vendors, 'products':products})
    # render(request template context)
    # return HttpResponse("Hello, world. You're at the polls index.")

##### SHOW PRODUCT ROUTE
def product(request, product_id):
    product = Product.objects.get(id=product_id)
    category = Category.objects.all()
#     form = QuestionForm()
#     # payload = {'key':'TOKEN'}
#     res = requests.get('http://thecatapi.com/api/images/get')
#     # res = requests.get('http://thecatapi.com/api/images/get', params=payload)
#     # return render(request, 'api.html', {'imageurl':res.url})
    return render(request, 'tbeystore/product.html', {'product':product, 'category':category})

##### CREATE PRODUCT ROUTE
def post_product(request, vendor_id):
    form = ProductForm(request.POST)
    vendor = Vendor.objects.get(id=vendor_id)
    # method on the form object
    if form.is_valid():
        product = form.save(commit = False)
        product.vendor = request.vendor
        product.save()
    return HttpResponseRedirect('/')

##### PROFILE ROUTE
def profile(request, user_name):
    user = User.objects.get(username=user_name)
    # vendor = Vendor.objects.filter(user=user)
    return render(request, 'tbeystore/profile.html', {'username':user_name})

##### VENDOR PROFILE ROUTE
def vendor(request, vendor_id):
    vendor = Vendor.objects.get(id=vendor_id)
    products = Product.objects.filter(vendor=vendor)
    # questions = Questions.objects.filter(products=products)
    form = ProductForm()
    # vendor_owner = User.objects.get(id=vendor.user_id)
    # print(vendor.id)
    # return render(request, 'tbeystore/vendor.html', {'vendor':vendor , 'user':vendor_owner})
    return render(request, 'tbeystore/vendor.html', {'vendor':vendor, 'products':products, 'form':form})
    # return render(request, 'tbeystore/vendor.html', {'vendor':vendor, 'form':form})

def vendor_signup(request, user_id):
    if request.method == 'POST':
        print('posting')
        form = VendorForm(request.POST)
        user = User.objects.get(id=user_id)
        # user_id = request.GET.get(id=user_id)
        print(user.id)
        if user is not None:
            if user.is_active:
                form.user_id = request.user.id
                print('we are posting a vendor')
                print(form.user_id)
                if form.is_valid():
                    print('form is valid')
                    # clean form
                    vendor = form.save()
                    vendor.save()
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

##### LIKE PRODUCT ROUTE
## TODO: add conditional for users ...............
def like_product(request):
    # print('like product view')
    product_id = request.GET.get('product_id', None)
    likes = 0
    if (product_id):
        product = Product.objects.get(id=int(product_id))
        if product is not None:
            likes = product.likes + 1
            product.likes = likes
            product.save()
    return HttpResponse(likes)

##### CAT PUT ROUTE
## TODO: add conditional for users ...............
# def edit_cat(request, cat_id):
#     instance = get_object_or_404(Cat, id=cat_id)
#     form = CatForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         form.save()
#         return redirect('show', cat_id)
#     return render(request, 'edit_cat.html', {'cat':instance, 'form':form})

##### CAT DELETE ROUTE
## TODO: add conditional for users ...............
# def delete_cat(request, cat_id):
#     if request.method == 'POST':
#         instance = Cat.objects.get(pk=cat_id)
#         instance.delete()
#         return redirect('index')

##### CREATE TOY ROUTE
# def create_toy(request, cat_id):
#     form = ToyForm(request.POST)
#     if form.is_valid():
#         # if we have good POST data
#         # see if there is a toy with this name
#         try:
#             toy = Toy.objects.get(name=form.data.get('name'))
#         except:
#             toy = None
#         #if no toy by that name exists save it to the database
#         if toy is None:
#             toy = form.save()
#         cat = Cat.objects.get(pk=cat_id)
#         toy.cats.add(cat)
#         return redirect('show_toy', toy.id)
#     else:
#         return redirect('show', cat_id)

##### SHOW TOY ROUTE
# def show_toy(request, toy_id):
#     toy = Toy.objects.get(pk=toy_id)
#     cats = toy.cats.all()
#     return render(request, 'show_toy.html', {'toy': toy, 'cats':cats})

### API ROUTE
# requests is a thing....for api calls
def api(request):
    # payload = {'key':'TOKEN'}
    res = requests.get('http://thecatapi.com/api/images/get')
    # res = requests.get('http://thecatapi.com/api/images/get', params=payload)
    return render(request, 'tbeystore/adverts.html', {'imageurl':res.url})


############
# Create your views here.

# Question “index” page – displays the latest few questions.
# Question “detail” page – displays a question text, with no results but with a form to vote.
# Question “results” page – displays results for a particular question.
# Vote action – handles voting for a particular choice in a particular question.
# In other words, your template should be at polls/templates/polls/index.html

class QuestionIndexView(generic.ListView):
    template_name = 'tbeystore/question.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # Return the last 5 published questions
        # not including those set for future publishing date
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        # return Question.objects.order_by('-pub_date')[:5]

class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'tbeystore/question_detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class QuestionResultsView(generic.DetailView):
    model = Question
    template_name = 'tbeystore/question_results.html'

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


# refactor ----
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list':latest_question_list}
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})

# 1 details
##########   -- refactor
# try:
#     question = Question.objects.get(pk=question_id)
# except Question.DoesNotExist:
#     raise Http404("Question does not exist")
# return render(request, 'polls/detail.html', {'question':question})

# - index
##########   -- refactor 3
# latest_question_list = Question.objects.order_by('-pub_date')[:5]
##########   -- refactor 2
# # output = ', '.join([q.question_text for q in latest_question_list])
##########
# template = loader.get_template('polls/index.html')
# context = {
#     'latest_question_list':latest_question_list,
# }
# return HttpResponse(template.render(context, request))
##########   -- refactor 1
# return HttpResponse("Hello, world. You're at the polls index.")
