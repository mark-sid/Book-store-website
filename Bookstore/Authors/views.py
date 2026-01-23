from django.db.models import Q
from .models import Author
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



class AuthorDetailView(DetailView):
    template_name = 'Authors/author_detail.html'
    model = Author
    context_object_name = 'author'




