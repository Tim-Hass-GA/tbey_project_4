from django.contrib import admin
from .models import Question, Choice, Vendor, Product, Category, Order, OrderItems

# Register your models here.

## stacked inline way
## modular view on top of one another
# class CategoryInLine(admin.StackedInline):
#     model = Category

class ProductInLine(admin.StackedInline):
    model = Product
    extra = 1

# class ProductAdmin(admin.ModelAdmin):
#     inlines = [CategoryInLine]

class VendorInLine(admin.StackedInline):
    model = Vendor
    ## how to display blank fields at the bottom of the stack
    ## to add new things......
    extra = 1

# _QUESTION AND CHOICE #
class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

## defind the way the view looks
class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 3

# import the model for the view
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]

## defind the way the view looks
class OrderItemsInLine(admin.StackedInline):
    model = OrderItems
    raw_id_field = ['product']

# import the model for the view
class OrderAdmin(admin.ModelAdmin):
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemsInLine]

# Register Choice and Question with their custom Admin interfaces
# add all admin views
# admin.site.register(Choice, ChoiceAdmin)
# update to include the view.....
admin.site.register(Question, QuestionAdmin)

# We haven't customized vendor. Register it as itself and take
# Django default admin interface.
# admin.site.register(Vendor, VendorAdmin)
admin.site.register(Vendor)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
admin.site.register(Category)
