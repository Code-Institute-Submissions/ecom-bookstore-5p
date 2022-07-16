from django.urls import path
import bookstoreadmin.views as bsav

urlpatterns = [
    path('', bsav.Index.as_view(), name='admin_index')
]