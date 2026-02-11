from django.db.models import Q
from .models import Author
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView


class AuthorsListView(ListView):
    template_name = 'Authors/authors_list.html'
    model = Author
    paginate_by = 10
    context_object_name = 'authors'
    ordering = ['birth_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search_query', None)

        if search_query:
            queryset = queryset.filter(
                Q(full_name__icontains=search_query)
            )

        return queryset

    @method_decorator(cache_page(60 * 60, key_prefix='book_list'))
    def get(self, *args, **kwargs):
        return super().get(self.request, *args, **kwargs)



class AuthorDetailView(DetailView):
    template_name = 'Authors/author_detail.html'
    model = Author
    context_object_name = 'author'

    @method_decorator(cache_page(60 * 60, key_prefix='book_list'))
    def get(self, *args, **kwargs):
        return super().get(self.request, *args, **kwargs)



