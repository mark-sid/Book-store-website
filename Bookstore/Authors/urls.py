from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorsListView.as_view(), name='authors_list'),
    path('authors/<slug:slug>', views.AuthorDetailView.as_view(), name='author_detail')

]