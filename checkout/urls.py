from django.urls import path
import checkout.views as cv

urlpatterns = [
    path('', cv.checkout.as_view(), name='checkout_page'),
    path(
        'payment/<int:order_id>',
        cv.checkout_payment.as_view(),
        name='checkout_payment'
    ),
    path('success/', cv.success.as_view(), name='checkout_success'),
    path('orders/', cv.orders.as_view(), name='see_orders'),
]
