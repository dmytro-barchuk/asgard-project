from django.urls import path
from . import views
from .views import NewsDetailView

app_name = 'news'
urlpatterns = [
	path('', views.NewsList.as_view(), name="news_list"),
	path('<slug:slug>', NewsDetailView.as_view(), name='news-detail'),
	path('create/', views.NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', views.NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', views.NewsDelete.as_view(), name='news_delete'),
] 