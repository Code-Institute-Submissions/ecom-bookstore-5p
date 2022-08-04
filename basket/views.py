from django.shortcuts import render, redirect
from django.views import View
from decimal import Decimal
from django.contrib import messages
import books.models as bkm
# Basket data stored as:
#   {'book_id': quantity(int)}

# TODO: This whole file can definatley be reduced to about 20 lines, or less
class index(View):
    def get(self, request):
        basket = {}
        total = 0

        if request.session.get('basket', False):
            basket = request.session['basket']
            total = request.session['total']

        template_data = []
        for key, value in basket.items():
            data = bkm.Book.objects.get(id=key)
            template_data.append((data, value))
        return render(
            request,
            'basket/index.html',
            {
                'basket': template_data,
                'total': total
            }
        )

class modify_class(View):
    def get(self, request, id, quantity, redirect_url='basket_index'):
        modify(request, id, quantity)
        if redirect_url == 'view_book':
            messages.success(request, 'Book has been added to basket!')
            return redirect(redirect_url, id)
        return redirect(redirect_url)

def modify(request, id, quantity):
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

class remove(View):
    def get(self, request, id):
        if str(id) in request.session['basket']:
            book = bkm.Book.objects.get(id=id)
            price_of_single = book.price * (1 - Decimal(book.discountPercent/100))
            request.session['total'] -= int(round(price_of_single * request.session['basket'][str(id)], 2)*100)
            del request.session['basket'][str(id)]
            messages.success(request, 'Book/s have been removed from your basket!')
            request.session.modified = True
        return redirect('basket_index')


class clear_view(View):
    def get(self, request):
        clear(request)
        return redirect('basket_index')

def clear(request):
    if request.session.get('basket', False):
        del request.session['basket']
    if request.session.get('total', False):
        del request.session['total']
    request.session.modified = True    