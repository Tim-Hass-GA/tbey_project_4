from django.contrib import admin
from .models import Question, Choice, Vendor

# Register your models here.

## stacked inline way
## modular view on top of one another
class VendorInLine(admin.StackedInline):
    model = Vendor
    ## how to display blank fields at the bottom of the stack
    ## to add new things......
    extra = 3

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


# Register Choice and Question with their custom Admin interfaces
# add all admin views
# admin.site.register(Choice, ChoiceAdmin)
# update to include the view.....
admin.site.register(Question, QuestionAdmin)

# We haven't customized vendor. Register it as itself and take
# Django default admin interface.
admin.site.register(Vendor)
