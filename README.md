# TBEY

Project 4 - GA

## About
TBEY is a small and niche market online store.  With an account users can purchase items from other user stores.  Users can currently only create one store (see next steps).

### Hosted App
coming soon...

## Technology Used
HTML, CSS, Materialize, Django, Python, jQuery/Ajax, Postgresql

## User Stories
- TBEY allows users to create an account to purchase products and services.
- TBEY allows small businesses to create a store for selling products and services.
- TBEY allows small businesses to interact with their clients asking them about upcoming products and services. (see next steps).

### CRUD Routes
Verb | Path | Action | Used for
------------ | ------------- | ------------ | -------------
GET | re_path('^$'... | read | - returns index/home page
GET | <int:product_id>/ | read | - returns product pro
GET | user/<user_name>/ | read | - returns user profile
GET (POST) | login/ | read (post) | - login view or login user
GET | logout/ | read | - logs user out
POST | signup/ | post | - create new user account
POST | post_product/<int:vendor_id>/'| post | - creates a new product
POST | like_product/ | post | - records a new like for product
PUT | <int:product_id>/edit_product/ | update | - edit a product
DELETE | <int:product_id>/destroy/ | delete | - delete a product
GET | vendor/<int:vendor_id> | read | - view store profile
POST | vendor_signup/<int:user_id>/ | post | - store signup
PUT | <int:vendor_id>/edit_vendor/ | update | - edit vendor profile
DELETE | <int:vendor_id>/destroy_vendor/ | delete | - delete a vendor
GET | cart_detail/ | read | - view cart detail
POST (PUT) | re_path('^add/(?P<product_id>\d+)/$ | post (update) | - add item to cart
DELETE | re_path('^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
POST | re_path('^create/$ | post | - create the order (submit)

## Views
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

### Data Models
![Image of DataModels](./readme_image/data_models.png)

### Wireframes
![Image of Wireframes](./readme_image/wireframe_0.png)
![Image of Wireframes](./readme_image/wireframe_1.png)
![Image of Wireframes](./readme_image/wireframe_2.png)
![Image of Wireframes](./readme_image/wireframe_3.png)

## Development Process

Fri - Day 1  (½ half day)
- Review ideas, draft some requirements,
- consider models and site structure
- Start boilerplate for wireframes and data models and user stories

Brainstorm ideas for project, decided on technologies, design wireframes, discussed data/model needs and app workflow.

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
- need to fix error handling on vendor route for attempts to add a second store.

## Next Steps - Unfinished Business
Things that were not completed or could be expanded upon within this app.

- Add more to readme...
- Edit route for user accounts
- Past Order summary for users
- Current Order summary for stores
- Add payment system
- Add images for products, user and stores
- Issue with refresh reorder
- More styling of user interface for better user experience.
- Connect to Ebay/Costco api to query related products for purchase or price comparison (user and store)

### Routes not in place
Verb | Path | Action | Used for
------------ | ------------- | ------------ | -------------
GET | question/ | read | - QuestionIndexView Route for user store to ask customers product question
GET | question/<int:pk>/ | read | - QuestionDetailView see specific question details
GET | question/<int:pk>/results/ | read | - QuestionResultsView see question results
PUT | question/<int:pk>/vote/ | update | no view provided - logs customers to vote ex: /question/5/vote
POST | comment/<int:product_id>/ | post | - create a comment for a product
