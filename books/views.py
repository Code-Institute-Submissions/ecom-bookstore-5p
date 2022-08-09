from difflib import SequenceMatcher
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from decimal import Decimal
from postoffice.forms import NotifySignUpForm
from postoffice.models import BookNotify
import books.forms as forms
import books.models as bkm


# https://stackoverflow.com/a/17388505
# TODO: apparently 'Token' and 'Someone' is 0.5, make more strict?
def similar(a, b):
    if a.lower() in b.lower() or b.lower() in a.lower():
        return 1
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


class index(View):
    def get(self, request):
        books = list(bkm.Book.objects.filter(available=True).order_by('id'))
        return render(
            request,
            'books/index.html',
            {
                'books': books[-3:]
            }
        )


class search(View):
    def get(self, request):
        form = forms.SearchForm()
        return render(
            request,
            'books/search.html',
            {
                'form': form
            }
        )


class results(View):
    def get(self, request):
        books = bkm.Book.objects.all()

        options = 0
        valid = []
        matches = []
        for b in books:
            # https://stackoverflow.com/a/19794198
            if request.GET.get('name'):
                options += 1
                rating = similar(request.GET.get('name'), b.name)
                if rating > 0.40:
                    valid.append(True)

            if request.GET.get('genre'):
                book_genres = bkm.BookGenre.objects.filter(book=b)
                book_genres = [x.genre.id for x in list(book_genres)]    
                options += 1
                if int(request.GET.get('genre')) in book_genres:
                    valid.append(True)

            if request.GET.get('author'):
                options += 1
                rating = similar(request.GET.get('author'), b.author)
                if rating > 0.40:
                    valid.append(True)

            if len([i for i in valid if i]) == options:
                g = bkm.BookGenre.objects.filter(book=b)
                matches.append([b, list(g)])
            valid = []
            options = 0
        return render(
            request,
            'books/results.html',
            {
                'data': matches
            }
        )


class view_book(View):
    def get(self, request, book_id):
        book = bkm.Book.objects.get(id=book_id)
        genres = bkm.BookGenre.objects.filter(book=book)

        price = book.price
        if book.discountPercent != 0:
            price = price * (1 - Decimal(book.discountPercent/100))
        price = format(price, ".2f")

        form = NotifySignUpForm()

        return render(
            request,
            'books/view.html',
            {
                'book_data': book,
                'book_genres': genres,
                'price': price,
                'form': form
            }
        )

    def post(self, request, book_id):
        form = NotifySignUpForm(request.POST)

        if form.is_valid():
            if BookNotify.objects.filter(email=request.user.email).exists():
                messages.warning(request, 'You Have Already Put A Watch On This Book!')
            else:
                new = BookNotify()
                if request.user.is_authenticated:
                    new.email = request.user.email
                else:
                    new.email = email

                new.book = bkm.Book.objects.get(id=book_id)            
                messages.success(request, 'You Will Be Notified When The Book Updates!')
                new.save()

        return HttpResponseRedirect(self.request.path_info)

