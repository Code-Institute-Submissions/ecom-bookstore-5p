from django.urls import path
import bookstoreadmin.views as bsav

urlpatterns = [
    path('', bsav.index.as_view(), name='admin_index'),
    path('books/', bsav.list_books.as_view(), name='list_books_admin'),
    path('books/modify/<int:book_id>', bsav.modify_book.as_view(), name='modify_book'),
    path('books/create/', bsav.create_book.as_view(), name='create_book'),
    path('books/delete/<int:book_id>', bsav.delete_book, name='delete_book'),
    path('genres/', bsav.list_genres.as_view(), name='list_genres_admin'),
    path('genres/create/', bsav.create_genre.as_view(), name='create_genre'),
    path('genres/modify/<int:genre_id>', bsav.modify_genre.as_view(), name='modify_genre'),
    path('genres/delete/<int:genre_id>', bsav.delete_genre, name='delete_genre'),
]
