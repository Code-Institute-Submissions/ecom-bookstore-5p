from django.shortcuts import render
from django.views import View
from django.conf import settings
import checkout.forms as forms
import books.models as bkm
import stripe
import os
if os.path.exists('env.py'):
    import env  # noqa


class checkout(View):
    def get(self, request):
        if request.session.get('basket', False):
            # os.environ.get('STRIPE_PUBLIC_KEY')
            # os.environ.get('STRIPE_SECRET_KEY')

            basket = request.session['basket']
            total = 0

            template_basket = []

            # Something wierd with price calc, idk why
            for bookid, quantity in basket.items():
                book = bkm.Book.objects.get(id=bookid)
                price = (float(book.price) * (1 - book.discountPercent/100)) * quantity
                total += price

                template_basket.append(
                    [
                        book.name,
                        book.price,
                        str(book.discountPercent) + '%',
                        quantity,
                        format(price, '.2f')
                    ]
                )
           
            stripe_total = round(total * 100)
            stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY
            )

            print(intent)
        else:
            basket = {}

        form = forms.OrderForm()

        return render(
            request,
            'checkout/checkout.html',
            {
                'stripe_public_key': os.environ.get('STRIPE_PUBLIC_KEY'),
                'client_secret': intent.client_secret,
                'template_basket': template_basket,
                'stripe_total': stripe_total,
                'form': form
            }
        )

    def post(self, request):
        pass
