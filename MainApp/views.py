from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов", 
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}

items = [
    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
    {"id": 7, "name": "Картофель фри" ,"quantity":0},
    {"id": 8, "name": "Кепка" ,"quantity":124},
]

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
    item = next((item for item in items if item['id'] == item_id), None)

    if item is not None:
        context = {
            "item": item
        }
        return render(request, "item_page.html", context)
    return HttpResponseNotFound(f"Item with id={item_id} not found")

def getitems(request):
    context = {
        "items": items
    }
    return render(request, "item_list.html", context)