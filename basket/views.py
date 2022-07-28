from django.shortcuts import render, redirect
from django.views import View
import books.models as bkm
from decimal import Decimal
# Basket data stored as:
#   {'book_id': quantity(int)}

class index(View):
    def get(self, request):
        basket = {}
        total = 0

        if request.session.get('basket', False):
            basket = request.session['basket']
            total = request.session['total']
        return render(
            request,
            'basket/index.html',
            {
                'basket': basket,
                'total': total
            }
        )


class modify(View):
    def get(self, request, id, quantity, redirect_url='basket_index'):
        if 'total' not in request.session:
            request.session['total'] = 0

        book = bkm.Book.objects.get(id=id)
        if not book.available or book.stock <= 0:
            return 
        price_of_single = book.price * (1 - Decimal(book.discountPercent/100))

        if request.session.get('basket', False):
            if str(id) in request.session['basket']:
                if request.session['basket'][str(id)] + quantity < 0:
                    quantity = -request.session['basket'][str(id)]

                request.session['total'] += int(round(price_of_single * quantity, 2)*100)
                request.session['basket'][str(id)] += quantity
            else:
                request.session['basket'][str(id)] = quantity
                request.session['total'] += int(round(price_of_single * quantity, 2)*100)

        else:
            request.session['basket'] = {}
            request.session['basket'][str(id)] = quantity
            request.session['total'] += int(round(price_of_single * quantity, 2)*100)

        if request.session['basket'][str(id)] <= 0:
            del request.session['basket'][str(id)]

        request.session.modified = True
        return redirect(redirect_url)


class remove(View):
    def get(self, request, id):
        if str(id) in request.session['basket']:
            book = bkm.Book.objects.get(id=id)
            request.session['total'] -= round((book.price * (1 - book.discountPercent)) * request.session['basket'][str(id)], 2)*100
            del request.session['basket'][str(id)]
            request.session.modified = True
        return redirect('basket_index')


class clear(View):
    def get(self, request):
        if request.session.get('basket', False):
            del request.session['basket']
        if request.session.get('total', False):
            del request.session['total']
            request.session.modified = True
        return redirect('basket_index')
