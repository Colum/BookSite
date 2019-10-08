from django.urls import path

from . import rest

urlpatterns = [
    path('', rest.get_all_books),
    path('<int:book_id>/', rest.get_book_by_id),
    path('checkout/<int:book_id>/', rest.checkout_book),
    path('return/<int:book_id>/', rest.return_book)
]