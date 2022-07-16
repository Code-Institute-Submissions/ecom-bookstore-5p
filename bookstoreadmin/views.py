from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
import books.models as bkm

PREFIX = 'bookstoreadmin/'
#region helpers
def check_admin(logged_user):
    return logged_user.is_superuser or Group.objects.filter(
            user=logged_user,
            name='site_admin'
        ).exists()


class index(View):
    def get(self, request):
        if check_admin(request.user):
            return render(request, PREFIX+'index.html')
        return redirect('books_index')
#endregion


#region books
class list_books(PermissionRequiredMixin, View):
    permission_required = 'books.view_book'

    def get(self, request):
        obj = bkm.Book.objects.all()
        return render(
            request,
            PREFIX+'books/books.html',
            {
                'obj': obj
            }
        )

    def post(self, request):
        pass


class create_book(PermissionRequiredMixin, View):
    permission_required = 'books.create_book'

    def get(self, request):
        pass

    def post(self, request):
        pass


class modify_book(PermissionRequiredMixin, View):
    permission_required = 'books.change_book'

    def get(self, request, book_id):
        return render(request, PREFIX+'modify.html')

    def post(self, request, book_id):
        return redirect('admin_index')

@permission_required('books.delete_book')
def delete_book(request, book_id):
    pass
#endregion

#region genres
class list_genres(PermissionRequiredMixin, View):
    permission_required = 'books.view_genre'

    def get(self, request):
        pass

class create_genre(PermissionRequiredMixin, View):
    permission_required = 'books.create_genre'

    def get(self, request):
        pass

    def post(self, request):
        pass

class modify_genre(PermissionRequiredMixin, View):
    permission_required = 'books.change_genre'

    def get(self, request):
        pass

    def get(self, request):
        pass

@permission_required('books.delete_genre')
def delete_genre(request, genre_id):
    pass
#endregion
