import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.vendor_name

    # def vendor_address(self):
    #     return self.address + self.city + self.state + self.zip

# CATEGORY CLASS #
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    date_added = models.DateField('date added', default=timezone.now)

    def __str__(self):
        return self.name
    def was_recently_added(self):
        now = timezone.now()
        return now - datetime.timedelta(days=10) <= self.date_added <= now

# PRODUCT CLASS #
class Product(models.Model):
    likes = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date_added = models.DateTimeField('date added', default=timezone.now)
    item_count = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def was_recently_added(self):
        now = timezone.now()
        return now - datetime.timedelta(days=10) <= self.date_added <= now

# COMMENTS CLASS #
class Comments(models.Model):
    comments = models.CharField(max_length=300)
    date_added = models.DateField('date added', default=timezone.now)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def was_recently_added(self):
        now = timezone.now()
        return now - datetime.timedelta(days=10) <= self.date_added <= now


# VENDOR PRODUCT CLASS #
class Vendor_Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # def __str__(self):
    # return self.name


# ORDER CLASS #       DO ME
# class Product_Order(models.Model):
#     user = models.OneToOneField(User)
#     product = models.ManyToManyField(Product)
#     item_count = models.PositiveIntegerField()


# _QUESTION CLASS #
class Question(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
