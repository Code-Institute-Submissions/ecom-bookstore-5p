from django.db import models
from books.models import Book

class BookNotify(models.Model):
    email = models.EmailField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Newsletter(models.Model):
    email = models.EmailField()
