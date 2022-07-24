from django.shortcuts import render
from django.views import View
import books.models as bkm 
import os
if os.path.exists('env.py'):
    import env  # noqa


class checkout(View):
    def get(self, request):
        if request.session.get('basket', False):
            basket = request.session['basket']
            total = 0
            prices = {}

            for bookid, quantity in basket.items():
                book =  bkm.Book.objects.get(id=bookid)
                price = (book.price * (1 - book.discountPercent)) * quantity
                total += price
                prices['bookid'] = price
            
            total = round(total * 100)
        else:
            basket = {}
        return render(
            request,
            'checkout/checkout.html',
            {
                'stripe_public_key': os.environ.get('STRIPE_PUBLIC_KEY'),
                'client_secret': 'hehe_secret key',
                'basket': basket,
                'prices': prices
            }
        )

    def post(self, request):
        pass
