from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()
        tags = self.request.query_params.get('tags', None)
        if tags:
            queryset = queryset.filter(tags__icontains=tags)
        return queryset

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
