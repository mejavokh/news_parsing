from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


def main_page(request):
    categories = Categories.objects.all()
    articles = Articles.objects.all()

    context = {
        'title': 'Главная страница',
        'categories': categories,
        'articles': articles
    }

    return render(request, 'main/index.html', context=context)


class BaseAPIView(APIView):
    model = None
    serializer_class = None

    def get(self, request):
        objects = self.model.objects.all()
        serializer = self.serializer_class(objects, many=True)
        return Response({self.model.__name__.lower() + 's': serializer.data})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({'error': 'Object does not exist'})

        serializer = self.serializer_class(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'put': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = self.model.objects.get(pk=pk)
            instance.delete()
        except self.model.DoesNotExist:
            return Response({'error': 'Object not found!'})

        return Response({'post': "delete post " + str(pk)})


class CategoryAPIView(BaseAPIView):
    model = Categories
    serializer_class = CategorySerializer


class ArticleAPIView(BaseAPIView):
    model = Articles
    serializer_class = ArticlesSerializer
