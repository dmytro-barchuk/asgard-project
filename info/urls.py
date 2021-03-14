from django.urls import path
from . import views


app_name = 'info'
urlpatterns = [
    path('payments/', views.PaymentList.as_view(), name="payments"),
    path('contacts/', views.ContactList.as_view(), name="contacts"),
	path('payments/create/', views.PaymentCreate.as_view(), name='payment_create'),
    path('payments/<int:pk>/update/', views.PaymentUpdate.as_view(), name='payment_update'),
    path('payments/<int:pk>/delete/', views.PaymentDelete.as_view(), name='payment_delete'),
    path('contacts/create/', views.ContactCreate.as_view(), name='contact_create'),
    path('contacts/<int:pk>/update/', views.ContactUpdate.as_view(), name='contact_update'),
    path('contacts/<int:pk>/delete/', views.ContactDelete.as_view(), name='contact_delete'),
] 