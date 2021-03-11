from django.urls import path
from . import views
from .views import ServiceDetailView
from django.views.generic import TemplateView



urlpatterns = [
	path('', TemplateView.as_view(template_name="main_page.html")),
	path('categories/', views.CategoryList.as_view()),
	path('services/', views.ServiceList.as_view(), name="service_list"),
	path('services/<slug:slug>', ServiceDetailView.as_view(), name='service-detail'),
	path('payment/', views.payment, name="payment"),
	path('contacts/', views.contacts, name="contacts"),
	path('comments/', views.comments_view, name="comments_view"),
	path('new_comment/', views.new_comment, name="new_comment"),
] 