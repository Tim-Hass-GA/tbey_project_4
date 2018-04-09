import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# CATEGORY CLASS #
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    date_added = models.DateField('date added')

    def __str__(self):
        return self.name


# PRODUCT CLASS #
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date_added = models.DateTimeField('date added')
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    item_count = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# COMMENTS CLASS #
class Comments(models.Model):
    comments = models.CharField(max_length=300)
    date_added = models.DateField('date added')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


# VENDOR CLASS #
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.PositiveIntegerField()
    website = models.URLField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.vendor_name

    # def vendor_address(self):
    #     return self.address + self.city + self.state + self.zip


# VENDOR PRODUCT CLASS #
class Vendor_Products(models.Model):
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    # def __str__(self):
    # return self.name


# ORDER CLASS #       DO ME
class Product_Order(models.Model):
    product = models.ManyToManyField(Product)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    item_count = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10000, decimal_places=2)


# _QUESTION CLASS #
class Question(models.Model):
    product = models.ManyToManyField(Product)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=10) <= self.pub_date <= now


# CHOICE CLASS #
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text



# ####### Create your models here.          CAT
# class Cat(models.Model):
#     likes = models.IntegerField(default=0)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     breed = models.CharField(max_length=100)
#     description = models.CharField(max_length=100)
#     age = models.IntegerField()
#     # toys = models.ManyToManyField(Toy)
#
#     def __str__(self):
#         return self.name
#
# class Toy(models.Model):
#     name = models.CharField(max_length=100)
#     cats = models.ManyToManyField(Cat)
#
#     def __str__(self):
#         return self.name

# # Create your models here            ARTIST.
# class Artist(models.Model):
#   name = models.CharField(max_length=200)
#
#   def __str__(self):
#     return self.name
#
# class Album(models.Model):
#   title = models.CharField(max_length=200)
#   artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#
#   def __str__(self):
#     return self.title
#
# class Song(models.Model):
#   title = models.CharField(max_length=200)
#   album = models.ForeignKey(Album, on_delete=models.CASCADE)
#   artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#
#   def __str__(self):
#     return self.title
