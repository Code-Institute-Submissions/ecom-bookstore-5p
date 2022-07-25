from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
import checkout.forms as forms
import books.models as bkm
import checkout.models as chm
import stripe
import os
if os.path.exists('env.py'):
    import env  # noqa


class checkout(View):
    def get(self, request):
        if request.session.get('basket', False):
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
           
            om = chm.Order()
            om.user = request.user

            om.save()
            for bookid, quantity in basket.items():
                basket_item = chm.OrderItem()
                basket_item.order = om
                basket_item.book = bkm.Book.objects.get(id=bookid)
                basket_item.quantity = quantity
                basket_item.priceOnPurchase = basket_item.book.price
                basket_item.save()

            form = forms.OrderForm({'order_id':om.id})
            # form.order_id = om.id
            return render(
                request,
                'checkout/checkout.html',
                {
                    'template_basket': template_basket,
                    'form': form
                }
            )            

        else:
            basket = {}
        # return 'you've got nothing in your basket!'
        pass

    def post(self, request):
        form = forms.OrderForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            data = chm.Order.objects.get(id=form.cleaned_data['order_id'])

            data.first_name = form.cleaned_data['first_name']
            data.second_name = form.cleaned_data['second_name']
            data.email = form.cleaned_data['email']
            # data.country = form.cleaned_data['country']
            data.postcode = form.cleaned_data['postcode']
            data.address_line_one = form.cleaned_data['address_line_one']
            data.town_city = form.cleaned_data['town_city']

            data.save()

            return redirect(
                'checkout_payment',
                order_id=form.cleaned_data['order_id']
            )
        # form failed
        print(form.errors)
        pass

class checkout_payment(View):
    def get(self, request, order_id):
        if request.session.get('basket', False):
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

            obj = chm.Order.objects.get(id=order_id)
            obj.payment_intent = intent['id']
            obj.save()

        else:
            basket = {}

        return render(
            request,
            'checkout/checkout_payment.html',
            {
                'stripe_public_key': os.environ.get('STRIPE_PUBLIC_KEY'),
                'client_secret': intent.client_secret,
                'template_basket': template_basket,
                'stripe_total': stripe_total
            }
        )
