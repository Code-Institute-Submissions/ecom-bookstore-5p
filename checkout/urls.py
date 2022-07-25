from django.urls import path
import checkout.views as cv

urlpatterns = [
    path('', cv.checkout.as_view(), name='checkout_page'),
    path('payment/<int:order_id>', cv.checkout_payment.as_view(), name='checkout_payment'),
]