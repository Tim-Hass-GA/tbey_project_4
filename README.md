# TBEY

## About
TBEY is a small and niche market online store.  With an account users can purchase items from other user stores.  Users can currently only create one store (see ).

### Hosted App
coming soon...

## User Stories



## Routes



  re_path('^$', views.index, name='index')
  path('<int:product_id>/', views.product, name='product'),
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
  path('cart_detail/', views.cart_detail, name='cart_detail'),
  re_path('^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
  re_path('^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
  re_path('^create/$', views.order_create, name='order_create'),
  path('api/', views.api, name='api'),

Store homepage – displays the latest few entries.
User Profile – displays the users data.
Profile update action – allows users to adjust profile data.
Product “detail” page – permalink page for a single entry.
Vendor Profile page – displays the vendors data.
Profile update action – allows users to adjust profile data.
Shopping Cart page – displays all months with entries in the given year..
Order page – displays all months with entries in the given year..
Order archive page – displays all months with entries in the given year..
Comment/Question action – handles posting comments to a given entry.
Question “detail” page – displays a question text, with no results but with a form to vote.
Question “results” page – displays results for a particular question.
Like action – handles liking for a particular product.


## Models

## Wireframes

## Development Process

Fri - Day 1  (½ half day)
- Review ideas, draft some requirements,
- consider models and site structure
- Start boilerplate for wireframes and data models and user stories

Saturday - Day 2
- django tutorial
- corrected issues with boilerplate template log in and sign up
- identified additional TODOs in boilerplate
- Create repo and create local file from boilerplate for project 4.

Sunday - Day 3
- models and views

Monday - Day 4
- Post Product Post vendor routes, site layout, improved views

Tuesday - Day 5
- Product and Vendor delete routes, logic for post product

Wednesday - Day 6
- Order Post and Delete routes, inventory changes
- ISSUE with post route, need to take into account edge cases for order  
- readme

Thursday - Day 7
- session and cart for order post, put and delete in place
- readme

Friday - Day 8 - Presentation

## Issues
- need to fix error handling on vendor route for attempt to add second store.


## Next Steps - Unfinished Business
Things that were not completed or could be expanded upon within this app.

- Add more to readme...
- Edit route for user accounts
- Add payment system
- Add images for products
- Issue with refresh reorder
- Connect to Ebay/Costco api to query related products for purchase or price comparison (user and store)

### Routes not in place
  question QuestionIndexView Route for User Store to ask customers product question
  question details question/<int:pk>/ QuestionDetailView see specific question details
  question/<int:pk>/results/' QuestionResultsView see question results
  question <int:question_id>/vote/ no view options customers to vote /question/5/vote
