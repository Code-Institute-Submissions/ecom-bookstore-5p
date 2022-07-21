from django.shortcuts import render, redirect
from django.views import View

# Basket data stored as:
#   {'book_id': quantity(int)}

class Index(View):
    def get(self, request):
        return render(request, 'basket/index.html')


class Add(View):
    def get(self, request):
        return redirect('basket_index')


class Remove(View):
    def get(self, request):
        return redirect('basket_index')


class Clear(View):
    def get(self, request):
        return redirect('basket_index')
