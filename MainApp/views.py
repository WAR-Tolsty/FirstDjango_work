from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from MainApp.models import Item

# Create your views here.
author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов", 
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}


def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "mymail@mail.com"
    }
    return render(request, "index.html", context)

def about(request):
    author = {
    "name": "Mikhail",
    "middle_name": "Nikolaevich",
    "last_name": "Stukaov",
    "phone": "9169066315",
    "email": "ya@mstukalov.ru"
    }
    return render(request, "about.html", {"author": author})

def getitem(request, item_id): 
    try:

        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Item with id={item_id} not found")
    else:
        context = {
            "item": item
        }
        return render(request, "item_page.html", context)
    

def getitems(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "item_list.html", context)