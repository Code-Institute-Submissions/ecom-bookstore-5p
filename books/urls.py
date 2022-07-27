from django.urls import path
import books.views as bkv

urlpatterns = [
    path('search/', bkv.search.as_view(), name='books_search'),
]