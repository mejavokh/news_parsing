from django.shortcuts import render

from .models import *


def main_page(request):
    categories = Categories.objects.all()
    articles = Articles.objects.all()

    context = {
        'title': 'Главная страница',
        'categories': categories,
        'articles': articles
    }

    return render(request, 'main/index.html', context=context)




