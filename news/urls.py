from django.urls import path
from . import views
from .views import NewsDetailView


urlpatterns = [
	path('news/', views.NewsList.as_view(), name="news_list"),
	path('news/<slug:slug>', NewsDetailView.as_view(), name='news-detail'),
] 