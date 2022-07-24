from django.urls import path
import checkout.views as cv

urlpatterns = [
    path('', cv.checkout.as_view(), name='checkout_page'),
]