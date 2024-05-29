from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Article, Comment, Category
from .serializers import (
    ArticleSerializer,
    CommentSerializer,
    CategorySerializer,
    LikeSerializer,
    CommentLikeSerializer,
)


class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Article.objects.all()
        tags = self.request.query_params.get("tags", None)
        category = self.request.query_params.get("category", None)
        if tags:
            queryset = queryset.filter(tags__icontains=tags)
        if category:
            queryset = queryset.filter(category__name=category)
        return queryset


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        article_id = self.kwargs["article_pk"]
        return Comment.objects.filter(article_id=article_id)

    def perform_create(self, serializer):
        article_id = self.kwargs["article_pk"]
        article = Article.objects.get(pk=article_id)
        serializer.save(article=article, author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ArticleLikeToggle(generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        article = self.get_object()
        user = request.user
        if user in article.likes.all():
            article.likes.remove(user)
        else:
            article.likes.add(user)
        return Response(self.get_serializer(article).data)


class ArticleDislikeToggle(generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        article = self.get_object()
        user = request.user
        if user in article.dislikes.all():
            article.dislikes.remove(user)
        else:
            article.dislikes.add(user)
        return Response(self.get_serializer(article).data)


class CommentLikeToggle(generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        comment = self.get_object()
        user = request.user
        if user in comment.likes.all():
            comment.likes.remove(user)
        else:
            comment.likes.add(user)
        return Response(self.get_serializer(comment).data)


class CommentDislikeToggle(generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        comment = self.get_object()
        user = request.user
        if user in comment.dislikes.all():
            comment.dislikes.remove(user)
        else:
            comment.dislikes.add(user)
        return Response(self.get_serializer(comment).data)
