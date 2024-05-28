from django.urls import path
from .views import ArticleListCreate, ArticleDetail
from .auth_views import RegisterAPI, login_api
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('articles/', ArticleListCreate.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', login_api, name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]