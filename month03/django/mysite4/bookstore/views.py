from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models


# Create your views here.
def add_view(request):
    if request.method == 'GET':
        return render(request, 'bookstore/add_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = request.POST.get('price')
        m_price = request.POST.get('m_price')
        try:
            models.Book.objects.create(
                title=title,
                pub=pub,
                price=price,
                market_price=m_price
            )
            # return HttpResponse("添加成功")
            return HttpResponseRedirect('/bookstore/get_all')
        except:
            return HttpResponse("添加失败")


def show_all_books(request):
    books = models.Book.objects.all()
    # for book in books:
    #     # print("书名", book.title, '出版社:', book.pub)
    #     print(book)
    # return HttpResponse("查询成功")
    return render(request, 'bookstore/list.html', {'books': books})


def update_book_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except:
        return HttpResponse("no data exists, book id is " + id)
    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html', {'abook': abook})
    elif request.method == 'POST':
        market_price = request.POST.get('market_price')
        abook.market_price = market_price
        abook.save()
        return HttpResponseRedirect('/bookstore/get_all')


def delete_book_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except:
        return HttpResponse("delete book failure, book id is " + id)
    abook.delete()
    return HttpResponseRedirect('/bookstore/get_all')


def set_cookies_view(request):
    resp = HttpResponse("ok")
    resp.set_cookie("my_var", 100, max_age=10)
    return resp


def get_cookies_view(request):
    val = request.COOKIES.get("my_var")
    return HttpResponse("val = " + str(val))
