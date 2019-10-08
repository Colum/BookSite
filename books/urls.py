from django.urls import path

from . import views

urlpatterns = [
    path('', views.books),
    path('<int:book_id>/', views.books_by_id),
    path('checkout/<int:book_id>/', views.checkout_book),
    path('return/<int:book_id>/', views.return_book)
]