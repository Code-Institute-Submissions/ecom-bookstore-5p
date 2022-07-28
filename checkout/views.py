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

# TODO: Only allow if logged in
class checkout(View):
    def get(self, request):
        if request.session.get('basket', False):
            basket = request.session['basket']

            template_basket = []

            total = 0

            status = True
            for bookid, quantity in basket.items():
                book = bkm.Book.objects.get(id=bookid)
                if book.stock == 0 or book.stock - quantity < 0 or not book.available:
                    status = False
                else:
                    status = True

                price = (float(book.price) * (1 - book.discountPercent/100)) * quantity
                total += price
                template_basket.append(
                    [
                        book.name,
                        book.price,
                        str(book.discountPercent) + '%',
                        quantity,
                        format(price, '.2f'),
                        status
                    ]
                )
        
            if len([h for h in template_basket if not h[5]]) == len(template_basket):
                return render(
                    request,
                    'checkout/checkout.html',
                    {
                        'template_basket': []
                    }
                )   

            form = forms.OrderForm({'order_id': 0})
            # form.order_id = om.id
            return render(
                request,
                'checkout/checkout.html',
                {
                    'total': total,
                    'template_basket': template_basket,
                    'form': form
                }
            )            

        else:
            basket = {}
            return render(
                request,
                'checkout/checkout.html',
                {
                    'template_basket': []
                }
            )   

    def post(self, request):
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            data = chm.Order()
            data.user = request.user

            data.first_name = form.cleaned_data['first_name']
            data.second_name = form.cleaned_data['second_name']
            data.email = form.cleaned_data['email']
            data.country = form.cleaned_data['country']
            data.postcode = form.cleaned_data['postcode']
            data.address_line_one = form.cleaned_data['address_line_one']
            data.town_city = form.cleaned_data['town_city']

            data.save()

            return redirect(
                'checkout_payment',
                order_id=data.id
            )
        # TODO: return error
        print(form.errors)
        pass


class checkout_payment(View):
    def get(self, request, order_id):
        if request.session.get('basket', False):
            basket = request.session['basket']
            total = 0

            for bookid, quantity in basket.items():
                book = bkm.Book.objects.get(id=bookid)
                if (book.stock == 0 or book.stock - quantity < 0 or not book.available):
                    continue
                price = (float(book.price) * (1 - book.discountPercent/100)) * quantity
                total += price

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
            # TODO: return error

        return render(
            request,
            'checkout/checkout_payment.html',
            {
                'stripe_public_key': os.environ.get('STRIPE_PUBLIC_KEY'),
                'client_secret': intent.client_secret,
                'stripe_total': stripe_total,
                'order_id': order_id
            }
        )


class success(View):
    def get(self, request):
        basket = request.session['basket']
        om = chm.Order.objects.get(payment_intent=request.GET.get('payment_intent'))

        for bookid, quantity in basket.items():
            book = bkm.Book.objects.get(id=bookid)
            book.stock -= quantity
            book.save()

            basket_item = chm.OrderItem()
            basket_item.order = om
            basket_item.book = bkm.Book.objects.get(id=bookid)
            basket_item.quantity = quantity
            basket_item.priceOnPurchase = basket_item.book.price
            basket_item.save()
        return render(request, 'checkout/success.html')


class orders(View):
    def get(self, request):
        stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

        orders = chm.Order.objects.filter(user=request.user)
        finished_orders = []
        for o in orders:
            pi = stripe.PaymentIntent.retrieve(o.payment_intent)
            if pi['status'] != 'succeeded':
                continue
            finished_orders.append(o)

        template_data = []
        for fo in finished_orders:
            new = [fo.id]
            new.append(list(chm.OrderItem.objects.filter(order=fo)))

            
