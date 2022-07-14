from django.urls import path
import books.views as bkv

urlpatterns = [
    path('', bkv.Index.as_view(), name='books_index')
]