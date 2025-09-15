from django.urls import path
from .views import books_list, reserve_book, reservations_list

urlpatterns = [
    path('books/', books_list, name='library_view'),
    path('books/<int:book_id>/reserve/', reserve_book, name='reserve_book'),
    path('books/reservations/', reservations_list, name='reservations_list'),
]