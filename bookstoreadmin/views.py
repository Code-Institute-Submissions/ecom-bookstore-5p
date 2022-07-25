from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group, User, Permission
from django.contrib.auth.decorators import permission_required
import books.models as bkm
import bookstoreadmin.forms as forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

try:
    if not Group.objects.filter(name='site_admin').exists():
        new_group, created = Group.objects.get_or_create(name='site_admin')
        perms = Permission.objects.filter(
                Q(content_type__app_label='books') |
                Q(content_type__app_label='checkout')
            )
        for p in perms:
            permission = Permission.objects.get(
                codename=p.codename,
                name=p.name,
                content_type=p.content_type
            )
            new_group.permissions.add(permission)
except:
    pass


PREFIX = 'bookstoreadmin/'
#region helpers
def check_admin(logged_user):
    return logged_user.is_superuser or Group.objects.filter(
            user=logged_user,
            name='site_admin'
        ).exists()
#endregion


class index(PermissionRequiredMixin, View):
    permission_required = 'book'

    def get(self, request):
        if check_admin(request.user):
            return render(request, PREFIX+'index.html')
        return redirect('books_index')


#region books
class list_books(PermissionRequiredMixin, View):
    permission_required = 'books.view_book'

    def get(self, request):
        data = bkm.Book.objects.all()
        obj = []
        for d in data:
            obj.append((d, bkm.BookGenre.objects.filter(book=d.id)))
        return render(
            request,
            PREFIX+'books/books.html',
            {
                'obj': obj
            }
        )


class create_book(PermissionRequiredMixin, View):
    permission_required = 'books.add_book'

    def get(self, request):
        form = forms.BookForm
        return render(
            request,
            PREFIX+'books/form.html',
            {
                'form': form
            }
        )

    def post(self, request):
        form = forms.BookForm(request.POST)
        if form.is_valid():
            data = bkm.Book()

            data.name = form.cleaned_data['name']
            data.description = form.cleaned_data['description']
            data.author = form.cleaned_data['author']
            data.pages = form.cleaned_data['pages']
            data.price = form.cleaned_data['price']
            data.owner = form.cleaned_data['owner']
            data.stock = form.cleaned_data['stock']
            data.discountPercent = form.cleaned_data['discountPercent']
            data.available = form.cleaned_data['available']

            data.save()
        return redirect('list_books_admin')


class modify_book(PermissionRequiredMixin, View):
    permission_required = 'books.change_book'

    def get(self, request, book_id):
        data = bkm.Book.objects.get(id=book_id)
        form = forms.BookForm(instance=data)

        return render(
            request,
            PREFIX+'books/form.html',
            {
                'form': form
            }
        )

    def post(self, request, book_id):
        form = forms.BookForm(request.POST)
        if form.is_valid():
            data = bkm.Book.objects.get(id=book_id)

            data.name = form.cleaned_data['name']
            data.description = form.cleaned_data['description']
            data.author = form.cleaned_data['author']
            data.pages = form.cleaned_data['pages']
            data.price = form.cleaned_data['price']
            data.owner = form.cleaned_data['owner']
            data.stock = form.cleaned_data['stock']
            data.discountPercent = form.cleaned_data['discountPercent']
            data.available = form.cleaned_data['available']

            data.save()
        return redirect('list_books_admin')


@permission_required('books.delete_book')
def delete_book(request, book_id):
    data = bkm.Book.objects.get(id=book_id)
    data.delete()
    return redirect('list_books_admin')


class modify_book_genres(PermissionRequiredMixin, View):
    permission_required = (
        'books.add_bookgenre',
        'books.change_bookgenre',
        'books.delete_bookgenre'
    )

    def get(self, request, book_id):
        obj = bkm.BookGenre.objects.filter(book=book_id)
        genres = bkm.Genre.objects.all()
        return render(
            request,
            PREFIX+'book_genres/modify.html',
            {
                'obj': obj,
                'genres': genres,
                'book_id': book_id
            }
        )

    def post(self, request, book_id):
        _book = bkm.Book.objects.get(id=book_id)

        data = request.POST.get('data').split('|')
        genres = bkm.Genre.objects.all()
        db_data = list(
            bkm
                .BookGenre
                .objects
                .filter(book=book_id)
                .values_list('genre__name', flat=True)
        )

        for _name in data:
            if _name not in db_data:
                model = bkm.BookGenre()
                model.book = _book
                model.genre = genres.get(name=_name)
                model.save()
            
        for name in db_data:
            if name not in data:
                value = bkm.BookGenre.objects.get(book=_book, genre__name=name)
                value.delete()
            

        return redirect('admin_index')
#endregion

#region genres
class list_genres(PermissionRequiredMixin, View):
    permission_required = 'books.view_genre'

    def get(self, request):
        data = bkm.Genre.objects.all()
        return render(
            request,
            PREFIX+'genres/genres.html',
            {
                'data': data
            }
        )


class create_genre(PermissionRequiredMixin, View):
    permission_required = 'books.add_genre'

    def get(self, request):
        form = forms.GenreForm()
        return render(
            request,
            PREFIX+'genres/form.html',
            {
                'form': form
            }
        )

    def post(self, request):
        form = forms.GenreForm(request.POST)
        if form.is_valid():
            data = bkm.Genre()
            data.name = form.cleaned_data['name']
            data.save()
        return redirect('list_genres_admin')


class modify_genre(PermissionRequiredMixin, View):
    permission_required = 'books.change_genre'

    def get(self, request, genre_id):
        data = bkm.Genre.objects.get(id=genre_id)
        form = forms.GenreForm(instance=data)

        return render(
            request,
            PREFIX+'genres/form.html',
            {
                'form': form
            }
        )

    def post(self, request, genre_id):
        form = forms.GenreForm(request.POST)
        if form.is_valid():
            data = bkm.Genre.objects.get(id=genre_id)
            data.name = form.cleaned_data['name']
            data.save()
        return redirect('list_genres_admin')


@permission_required('books.delete_genre')
def delete_genre(request, genre_id):
    data = bkm.Genre.objects.get(id=genre_id)
    data.delete()
    return redirect('list_genres_admin')
#endregion
