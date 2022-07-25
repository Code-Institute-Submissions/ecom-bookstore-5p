from django.db import models
from django.contrib.auth.models import User
from books.custom_models import IntegerRangeField


class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # eBookPrice
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    # image
    stock = models.IntegerField()
    # isOnSale probably not needed as, if below is not empty then its on sale
    discountPercent = IntegerRangeField(min_value=0, max_value=100)
    available = models.BooleanField(default=True)


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)