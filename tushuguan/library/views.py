from django.shortcuts import render
from django.http import HttpResponse
from .models import book
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def home(request):
    bookList = book.objects.all()
    paginator = Paginator(bookList,2,1)
    try:
        page = request.GET.get('page')
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request, 'home/index.html',{"title":"首页","bookList":bookList,"customer":customer})

def add_book(request):
    return render(request, 'add_book/add.html',{"title":"添加书籍"})


from django.http import HttpResponseRedirect
def add(request):
    add_book = request.POST.get("book","")
    add_price = request.POST.get("price", "")
    add_date = request.POST.get("date", "")
    add_press = request.POST.get("press","")
    add_auther = request.POST.get("auther","")
    #添加书的名称
    Book = book()
    Book.bookName = add_book
    Book.price = add_price
    Book.publication = add_date
    Book.press = add_press
    Book.auther = add_auther
    Book.save()
    return HttpResponseRedirect('succeed')

def succeed(request):
    return render(request, 'succeed.html')

