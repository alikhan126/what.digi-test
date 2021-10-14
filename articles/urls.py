from django.urls import path

from articles import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='articles'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
]
