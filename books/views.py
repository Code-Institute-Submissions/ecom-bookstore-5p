from difflib import SequenceMatcher
from django.shortcuts import render
from django.views import View
from decimal import Decimal
import books.forms as forms
import books.models as bkm

# https://stackoverflow.com/a/17388505
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


class index(View):
    def get(self, request):
        return render(request, 'books/index.html')


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

    def post(self, request):
        form = forms.SearchForm(request.POST)

        if form.is_valid():
            books = bkm.Book.objects.all()

            valid = False
            matches = []
            for b in books:
                # https://stackoverflow.com/a/19794198
                if form.cleaned_data['name']:
                    rating = similar(form.cleaned_data['name'], b.name)
                    valid = rating > 0.75

                book_genres = bkm.BookGenre.objects.filter(book=b)
                book_genres = [x.genre.id for x in list(book_genres)]
                if form.cleaned_data.get('genre') is not None:
                    valid = form.cleaned_data.get('genre').id in book_genres

                if form.cleaned_data['author']:
                    rating = similar(form.cleaned_data['author'], b.author)
                    valid = rating > 0.75

                if valid:
                    g = bkm.BookGenre.objects.filter(book=b)
                    matches.append([b, list(g)])

            return render(
                request,
                'books/results.html',
                {
                    'data': matches
                }
            )
        return render(
            request,
            'books/search.html',
            {
                'form': form
            }
        )


class view_book(View):
    def get(self, request, book_id):
        book = bkm.Book.objects.get(id=book_id)
        genres = bkm.BookGenre.objects.filter(book=book)

        price = book.price
        if book.discountPercent != 0:
            price = price * (1 - Decimal(book.discountPercent/100))
        price = "£"+format(price, ".2f")

        return render(
            request,
            'books/view.html',
            {
                'book_data': book,
                'book_genres': genres,
                'price': price
            }
        )