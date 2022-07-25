from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from django_countries.fields import CountryField


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now=True)

    first_name = models.CharField(max_length=30, null=True)
    second_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(blank=False, null=True)
    country = CountryField(null=True)

    payment_intent = models.CharField(max_length=500, null=True)
    success = models.BooleanField(default=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    priceOnPurchase = models.DecimalField(max_digits=6, decimal_places=2)
    isEBook = models.BooleanField(default=False)
    quantity = models.IntegerField()