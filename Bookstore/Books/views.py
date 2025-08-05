from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from Cart.forms import CartAddBookForm
from . forms import CategorySelectForm
from .models import Book, Category


# Create your views here.


class BookListView(ListView):
    template_name = 'Books/books_list.html'
    model = Book
    paginate_by = 10
    context_object_name = 'books'
    ordering = ['published_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(available=True)

        category_slug = self.request.GET.get('category_slug')

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        form = CategorySelectForm(self.request.GET or None, categories=categories)
        context['form'] = form

        return context


class BookDetailView(DetailView):
    template_name = 'Books/book_detail.html'
    model = Book
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartAddBookForm()
        return context
