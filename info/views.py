from django.views.generic import ListView
from info.models import Payment, Contact
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 

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
class PaymentCreate(UserPassesTestMixin, CreateView):
    model = Payment
    fields = ['name', 
    'describe',
    ]
    success_url = '/info/payments'

    def test_func(self):
        return self.request.user.username == 'admin'

class PaymentUpdate(UserPassesTestMixin, UpdateView):
    model = Payment
    fields = ['name', 
    'describe',
    ]
    success_url = '/info/payments'

    def test_func(self):
        return self.request.user.username == 'admin'

class PaymentDelete(UserPassesTestMixin, DeleteView):
    model = Payment
    success_url = reverse_lazy('info:payments')

    def test_func(self):
        return self.request.user.username == 'admin'

# CRUD CONTACTS
class ContactCreate(UserPassesTestMixin, CreateView):
    model = Contact
    fields = ['name', 
    'describe',
    ]
    success_url = '/info/contacts'
    
    def test_func(self):
        return self.request.user.username == 'admin'

class ContactUpdate(UserPassesTestMixin,UpdateView):
    model = Contact
    fields = ['name', 
    'describe',
    ]
    success_url = '/info/contacts'

    def test_func(self):
        return self.request.user.username == 'admin'

class ContactDelete(UserPassesTestMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('info:contacts')

    def test_func(self):
        return self.request.user.username == 'admin'

