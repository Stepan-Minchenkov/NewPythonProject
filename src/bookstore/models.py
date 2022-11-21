from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, null=True, upload_to='covers/%Y/%m/%d')
    price = models.DecimalField(decimal_places=2, max_digits=5)
    authors = models.ForeignKey('reference.Author', on_delete=models.PROTECT, related_name='book')
    series = models.ForeignKey('reference.Serie', on_delete=models.PROTECT, related_name='book', blank=True, null=True)
    genre = models.ForeignKey('reference.Genre', on_delete=models.PROTECT, related_name='book')
    publish_year = models.CharField(max_length=4, default=datetime.now().date().year)
    number_of_pages = models.IntegerField()
    cover = models.CharField(max_length=20)
    book_format = models.CharField(max_length=20, blank=True, null=True, default='')
    ISBN = models.CharField(max_length=30)
    weight = models.IntegerField()
    allowed_age = models.IntegerField(blank=True, null=True, default=0)
    publisher = models.ForeignKey('reference.Publisher', on_delete=models.PROTECT, related_name='book')
    available = models.IntegerField()
    active = models.BooleanField(default='Yes')
    rate = models.IntegerField(blank=True, null=True, default=0)
    created = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name:20}  {self.authors.name:20}"


class GoodsInBasket(models.Model):
    order = models.CharField(max_length=100)
    article = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='goodsinbasket')
    number = models.IntegerField()
    total_sum = models.DecimalField(decimal_places=2, max_digits=6)
    created = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.order

    def __repr__(self):
        return f"{self.order:20}  {self.article.name:20}  {self.created:20}  {self.updated:20}"


User_min_data = get_user_model()


class Customer(models.Model):
    user_data = models.OneToOneField(User_min_data, on_delete=models.PROTECT, related_name='customer')
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=20)
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user_data.username

    def __repr__(self):
        return f"{self.user_data.username:20} "


class Basket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='customer', default='Anonymous')
    goods = models.ForeignKey(GoodsInBasket, on_delete=models.PROTECT, related_name='basket')
    created = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.customer

    def __repr__(self):
        return f"{self.customer:20}  {self.created:20}  {self.updated:20}"
