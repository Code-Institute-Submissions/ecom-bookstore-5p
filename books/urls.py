from django.urls import path
import books.views as bkv

urlpatterns = [
    path('', bkv.search.as_view(), name='books_index')
]