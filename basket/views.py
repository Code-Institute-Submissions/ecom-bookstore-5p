from django.shortcuts import render, redirect
from django.views import View

# Basket data stored as:
#   {'book_id': quantity(int)}


class Index(View):
    def get(self, request):
        if request.session.get('basket', False):
            print(request.session['basket'])
        return render(
            request,
            'basket/index.html',
            {
                'basket': request.session['basket']
            }
        )


class Add(View):
    def get(self, request):
        return redirect('basket_index')


class Remove(View):
    def get(self, request):
        return redirect('basket_index')


class Clear(View):
    def get(self, request):
        return redirect('basket_index')
