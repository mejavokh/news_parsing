from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('categories/', CategoryAPIView.as_view()),
    path('articles/', ArticleAPIView.as_view()),
]
