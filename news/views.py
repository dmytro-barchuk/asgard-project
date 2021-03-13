from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import News


# Создаем представление для отображения списка всех категорий (хотя их в проекте только 2)
class NewsList(ListView):
    model = News
    context_object_name = 'news_list'
    queryset = News.objects.all().order_by('-updated')

class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#CRUD!!!

class NewsCreate(CreateView):
    model = News
    fields = ['news_title', 
    'image',
    'body',
    ]
    success_url = '/news'

class NewsUpdate(UpdateView):
    model = News
    fields = ['news_title', 
    'image',
    'body',
    ]
    success_url = '/news'

class NewsDelete(DeleteView):
    model = News
    success_url = reverse_lazy('news:news_list')