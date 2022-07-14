from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    priceOnPurchase = models.DecimalField(max_digits=6, decimal_places=2)
    isEBook = models.BooleanField(default=False)
    quantity = models.IntegerField()