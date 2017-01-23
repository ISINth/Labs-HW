from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .forms import UserForm, BookForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Book, Book_User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.http import HttpResponse


# Create your views here.

def auth(request):
    if not request.user.is_authenticated():
        error = ""
        if request.method == "POST":
            form=UserForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if request.POST.get('reg'):
                    if User.objects.filter(username=username).exists():
                        error = "Пользователь с таким логином уже существует"
                    else:
                        var=User(username=username)
                        var.save()
                        var = User.objects.get(username=username)
                        var.set_password(password)
                        var.save()
                        user = authenticate(username=username, password=password)
                        login(request,user)
                        return redirect('main')
                elif user is not None:            
                    if user.is_active:
                        login(request, user)
                        return redirect('main')
                else:
                    form = UserForm()
                    error = "Неправильный логин или пароль"
        else:
            form = UserForm()
        return render(request, 'bookshop/auth.html',{'form': form, 'error':error})
    else:
        return redirect('auth')


def main(request):
    if request.user.is_staff:
        admin = True;
    else:
        admin = False
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 4)  # Show 4 contacts per page
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginator = Paginator(book_list, 8)
        books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book=form.save(commit=False)
            book.save()
            return redirect('info',pk=book.pk)
    else:
        form=BookForm()
    
    if request.GET.get('ajax'):
        data = {}
        data['list'] = list()
        for book in books:
            inf = {}
            inf['pk'] = book.pk
            inf['name'] = book.name
            inf['author'] = book.author
            inf['img'] = book.img.url[8:]
            data['list'].append(inf)
        data['max']=paginator.num_pages            
        return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request, 'bookshop/main.html',{"books":books,'admin':admin, 'form':form})


def info(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user_list = Book_User.objects.filter(book=pk)
    log_in = request.user.is_authenticated()
    if request.method == "POST":
        username = request.user.username
        if book.number > 0:
            if Book_User.objects.filter(user=username, book=pk).exists():
                b_u = Book_User.objects.get(user=username, book=pk)
                b_u.number += 1
                b_u.save()
            else:
                b_u=Book_User(user=username,book=pk, number=1)
                b_u.save()
            book.number -= 1
            book.save()
        data = {}
        data['num'] = book.number
        us_l = {}
        for user in user_list:
            if user.user == username:
                us_l['user'] = user.user
                us_l['number'] = user.number
        data['us_l'] = us_l
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return render(request, 'bookshop/info.html', {'book': book, 'user_list': user_list,"log_in": log_in})


def edit(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('main', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'bookshop/edit.html',{'form': form})
