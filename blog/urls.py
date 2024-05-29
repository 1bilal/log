from django.urls import path
from .views import (
    ArticleListCreate,
    ArticleDetail,
    CommentListCreate,
    CommentDetail,
    CategoryListCreate,
    CategoryDetail,
    ArticleLikeToggle,
    ArticleDislikeToggle,
    CommentLikeToggle,
    CommentDislikeToggle,
)
from .auth_views import RegisterAPI, login_api
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("articles/", ArticleListCreate.as_view(), name="article-list-create"),
    path("articles/<int:pk>/", ArticleDetail.as_view(), name="article-detail"),
    path(
        "articles/<int:article_pk>/comments/",
        CommentListCreate.as_view(),
        name="comment-list-create",
    ),
    path(
        "articles/<int:article_pk>/comments/<int:pk>/",
        CommentDetail.as_view(),
        name="comment-detail",
    ),
    path("categories/", CategoryListCreate.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryDetail.as_view(), name="category-detail"),
    path("articles/<int:pk>/like/", ArticleLikeToggle.as_view(), name="article-like"),
    path(
        "articles/<int:pk>/dislike/",
        ArticleDislikeToggle.as_view(),
        name="article-dislike",
    ),
    path("comments/<int:pk>/like/", CommentLikeToggle.as_view(), name="comment-like"),
    path(
        "comments/<int:pk>/dislike/",
        CommentDislikeToggle.as_view(),
        name="comment-dislike",
    ),
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", login_api, name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
