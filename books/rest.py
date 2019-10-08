from django.http import HttpResponse
from .models import Book
from django.core import serializers
from django.forms.models import model_to_dict
from django.views.decorators.http import *
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json

# todo move to response message to dedicated class
not_found_body = {'message': 'book not found'}
ok_body = {'message': 'request ok'}
book_checked_out_body = {'message': 'book already checked out'}
book_not_checkout_out_body = {'message': 'book not checked out; cannot return'}


@require_GET
def get_all_books(request):
    page_num = request.GET.get('page') if request.GET.get('page') is not None else 1
    rating = request.GET.get('rating') if request.GET.get('rating') is not None else 0
    order_by = request.GET.get('orderby')

    if order_by not in ['book_authors', 'book_format', 'book_title']:
        order_by = 'id'

    book_list = Book.objects.filter(book_rating__gte=rating).order_by(order_by)

    paginator = Paginator(book_list, 25)  # Show 25 books per page
    book_page = paginator.get_page(page_num)

    json_list = serializers.serialize('json', book_page)
    return create_http_response(json_list)


@require_GET
def get_book_by_id(request, book_id):
    try:
        result = Book.objects.get(pk=book_id)
        dict_obj = model_to_dict(result)
        return create_http_response(dict_obj)
    except Book.DoesNotExist:
        return create_http_response(not_found_body, 404)


@require_POST
@csrf_exempt
def checkout_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        if book.checked_out:
            return create_http_response(book_checked_out_body, 400)
        else:
            book.checked_out = True
            book.save()
            return create_http_response(ok_body)
    except Book.DoesNotExist:
        return create_http_response(not_found_body, 404)


@require_POST
@csrf_exempt
def return_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        if book.checked_out:
            book.checked_out = False
            book.save()
            return create_http_response(ok_body)
        else:
            return create_http_response(book_not_checkout_out_body, 400)
    except Book.DoesNotExist:
        return create_http_response(not_found_body, 404)


def create_http_response(body_dict, http_code=200):
    if type(body_dict) is str:
        formatted_body = body_dict
    else:
        formatted_body = json.dumps(body_dict)
    return HttpResponse(formatted_body, content_type='application/json', status=http_code)

