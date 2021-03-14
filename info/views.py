from django.views.generic import ListView
from info.models import Payment, Contact
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Создаем представление для отображения списка всех категорий (хотя их в проекте только 2)
class PaymentList(ListView):
    model = Payment
    context_object_name = 'payment_list'
    queryset = Payment.objects.filter(active=True)

class ContactList(ListView):
    model = Contact
    context_object_name = 'contact_list'
    queryset = Contact.objects.filter(active=True)

# CRUD PAYMENT
class PaymentCreate(CreateView):
    model = Payment
    fields = ['name', 
    'describe',
    ]
    success_url = '/info/payments'

class PaymentUpdate(UpdateView):
    model = Payment
    fields = ['name', 
    'describe',
    ]
    success_url = '/info/payments'

class PaymentDelete(DeleteView):
    model = Payment
    success_url = reverse_lazy('info:payments')

# CRUD CONTACTS
class ContactCreate(CreateView):
    model = Contact
    fields = ['name', 
    'describe',
    ]
    success_url = '/info/contacts'

class ContactUpdate(UpdateView):
    model = Contact
    fields = ['name', 
    'describe',
    ]
    success_url = '/info/contacts'

class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('info:contacts')