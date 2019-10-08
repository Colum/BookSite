from django.http import HttpResponse
from .models import Book
from django.core import serializers
from django.forms.models import model_to_dict
import json


# todo move to response message class
not_found_body = {'message': 'not found'}
ok_body = {'message': 'request ok'}
book_checked_out_body = {'message': 'book already checked out'}
book_not_checkout_out_body = {'message': 'book not checked out; cannot return'}


def books(request):
    print(request.GET)
    for query in request.GET:
        print(query + ' ' + request.GET[query])
    return HttpResponse('You made a request for all the books')


def books_by_id(request, book_id):
    result = Book.objects.get(pk=book_id)
    dict_obj = model_to_dict(result)
    return create_http_response(dict_obj)


def checkout_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if book.checked_out:
        return create_http_response(book_checked_out_body, 400)
    else:
        book.checked_out = True
        book.save()
        return create_http_response(ok_body)


def return_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if book.checked_out:
        book.checked_out = False
        book.save()
        return create_http_response(ok_body)
    else:
        return create_http_response(book_not_checkout_out_body, 400)


def create_http_response(body_dict, http_code=200):
    return HttpResponse(json.dumps(body_dict), content_type='application/json', status=http_code)

