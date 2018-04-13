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
    zip = models.CharField(max_length=5)
    website = models.URLField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=9)

    def __str__(self):
        return self.vendor_name

    def show_vendor_address(self):
        address = self.address, self.city, self.state, str(self.zip)
        return address

# CATEGORY CLASS #
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    date_added = models.DateField('date added', default=timezone.now)

    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    def was_recently_added(self):
        now = timezone.now()
        return now - datetime.timedelta(days=10) <= self.date_added <= now

# PRODUCT CLASS #
class Product(models.Model):
    likes = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date_added = models.DateTimeField('date added', default=timezone.now)
    item_count = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    available = models.BooleanField(default=True)
    # type = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='tbeystore/static/tbeystore/images/products', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    # class Meta:
    #     ordering = ('-created',)

    def __str__(self):
        return self.name
    def was_recently_added(self):
        now = timezone.now()
        return now - datetime.timedelta(days=10) <= self.date_added <= now
    # def get_absolute_url(self):
    #     return reverse('tbeystore:product', args=[self.id])

# COMMENTS CLASS #
class Comments(models.Model):
    comment = models.CharField(max_length=300)
    date_added = models.DateField('date added', default=timezone.now)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    def was_recently_added(self):
        now = timezone.now()
        return now - datetime.timedelta(days=10) <= self.date_added <= now



# ORDER CLASS #
class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    # city = models.CharField(max_length=100)
    # state = models.CharField(max_length=2)
    # zip = models.CharField(max_length=5)
    created = models.DateField('date created', default=timezone.now)
    updated = models.DateField('date updated', default=timezone.now)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return 'Order {}'.format(self.id)
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

# ORDER ITEMS CLASS #
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.id)
    def get_cost(self):
        return self.price * self.quantity


## initial order model
class Product_Order(models.Model):
    # vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.PositiveIntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # order_invoice = models.FileField(upload_to='tbeystore/static/tbeystore/user/invoice')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.CharField(max_length=200, default="placeholder")


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
        return now - datetime.timedelta(days=30) <= self.pub_date <= now


# CHOICE CLASS #
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
