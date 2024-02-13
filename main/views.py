from django.shortcuts import render, redirect
from main.forms import BookForm
from main.models import Book
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def show_main(request):
    books = Book.objects.all()

    context = {
        'name': 'A. Nurcahaya Tampubolon',
        'class': 'PBP A Genap',
        'books': books
    }

    return render(request, "main.html", context)

def create_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_book.html", context)

def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_book_id(request, book_id):
    data = Book.objects.filter(pk=book_id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_book_id(request, book_id):
    data = Book.objects.filter(pk=book_id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")