from django.urls import path
from . import views
from .views import ServiceDetailView
from django.views.generic import TemplateView


urlpatterns = [
	path('', TemplateView.as_view(template_name="main_page.html")),
	path('categories/', views.CategoryList.as_view()),
	path('services/', views.ServiceList.as_view(), name="service_list"),
	path('services/<int:id>', views.CategoryServiceList.as_view(), name="service_list_by_category"),
	path('services/<slug:slug>', ServiceDetailView.as_view(), name='service-detail'),
	path('comments/', views.comments_view, name="comments_view"),
	path('new_comment/', views.new_comment, name="new_comment"),
	path('<int:pk>/del_comment/', views.CommentDelete.as_view(), name="del_comment"),
] 