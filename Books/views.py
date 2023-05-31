# from __future__ import unicode_literals
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.core import serializers

from django.views.decorators.http import require_http_methods

from .models import Book


# Create your views here.

# add_book接受一个get请求，往数据库里添加一条book数据
@require_http_methods(['GET'])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'),book_author=request.GET.get('book_author'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


# show_books返回所有的书籍列表（通过JsonResponse返回能被前端识别的json格式数据）
@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


""" # delete_book删除对应列表的一条书籍数据（通过JsonResponse返回能被前端识别的json格式数据）
@require_http_methods(["DELETE"])
def delete_book(request):
    response = {}
    try:
        books = Book.delete()

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response) """
