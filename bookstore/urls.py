from django.contrib import admin
from django.urls import path, include
import books.views as bv
from .views import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('books/', include('books.urls')),
    path('bookstoreadmin/', include('bookstoreadmin.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('postoffice/', include('postoffice.urls')),
    path('', bv.index.as_view(), name='index_bookstore'),
]

handler404 = 'bookstore.views.handler404'
