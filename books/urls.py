from django.urls import path
import books.views as bkv

urlpatterns = [
    path('search/', bkv.search.as_view(), name='books_search'),
    path('view/<int:book_id>', bkv.view_book.as_view(), name='view_book'),
]