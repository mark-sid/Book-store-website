from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from Books.models import Book
from .cart import Cart
from .forms import CartAddBookForm


def cart_detail(request):
    template_name = 'Cart/cart_detail.html'
    cart = Cart(request)

    return render(request, template_name, {'cart': cart})

@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    form = CartAddBookForm(request.POST)

    if form.is_valid():
        cart.add(
            book=book,
            quantity=form.cleaned_data['quantity'],
            update_quantity=form.cleaned_data['update']
        )

    return redirect('cart')


def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)

    return redirect('cart')