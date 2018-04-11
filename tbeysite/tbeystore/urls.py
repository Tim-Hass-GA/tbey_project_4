from django.urls import path, re_path
from . import views

# path(path / urls / kwargs / name)
# re_path regular expression
# path( r'^([0-9]+)/$'
# match path 1-9 do not include anything after
# another way with path to get a specific index and show it

# path('<int:cat_id>/', views.show, name='show
# path('<int:cat_id>/edit/', views.edit_cat, name='edit_cat'),
# path('<int:cat_id>/destroy/', views.delete_cat, name='delete_cat'),

# map the views
app_name = 'tbeystore'
urlpatterns = [
    re_path('^$', views.index, name='index'),
    # path('', views.IndexView.as_view(), name='index'),
    # re_path(r'^([0-9]+)/$', views.show, name='show'),
    path('<int:product_id>/', views.product, name='product'),
    # path('<int:vendor_id>/post_product/', views.post_product, name='post_product'),
    path('post_product/<int:vendor_id>/', views.post_product, name='post_product'),
    path('user/<user_name>/', views.profile, name='profile'),
    path('vendor/<int:vendor_id>/', views.vendor, name='vendor'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('vendor_signup/<int:user_id>/', views.vendor_signup, name='vendor_signup'),
    path('like_product/', views.like_product, name='like_product'),
    path('<int:product_id>/add_to_order/<int:user_id>/', views.add_to_order, name='add_to_order'),
    path('<int:product_id>/edit_product/', views.edit_product, name='edit_product'),
    path('<int:vendor_id>/edit_vendor/', views.edit_vendor, name='edit_vendor'),
    path('<int:product_id>/destroy/', views.delete_product, name='delete_product'),
    path('<int:vendor_id>/destroy_vendor/', views.delete_vendor, name='delete_vendor'),
    # path('<int:cat_id>/toy/create/', views.create_toy, name='create_toy'),
    # path('toy/<int:toy_id>/', views.show_toy, name='show_toy'),
    path('api/', views.api, name='api'),
    # /question/
    path('question', views.QuestionIndexView.as_view(), name='question'),
    # /question/5/
    path('question/<int:pk>/', views.QuestionDetailView.as_view(), name='question_detail'),
    # /question/5/results
    path('question/<int:pk>/results/', views.QuestionResultsView.as_view(), name='question_results'),
    # /question/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
