from django.shortcuts import render, redirect
from django.http import HttpResponse # Убрать когда не нужно тестить
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from service.models import Category, Service, Comment
from service.forms import CommentForm


def main_page(request):
    hello = "WELCOME to site"
    return HttpResponse(hello)

# Создаем представление для отображения списка всех категорий (хотя их в проекте только 2)
class CategoryList(ListView):
	model = Category
	context_object_name = 'category_list'

class ServiceList(ListView):
	model = Service
	context_object_name = 'service_list'
	# Упорядочивание по дате публикации
	queryset = Service.objects.select_related('category').order_by('category', '-updated')

def comments_view(request):
    comments = Comment.objects.filter(active=True).order_by('-created')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request, 'service/comment_list.html', {'form': form})
    else:
        form = CommentForm()

    return render(request, 'service/comment_list.html', {'comments': comments, 'form': form})

def new_comment(request):
    form = CommentForm()
    context = {'form': form}

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/comments')
    return render(request, 'forms/new_comment.html', {'form': form})

class ServiceDetailView(DetailView):
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def payment(request):
    return render(request, 'service/payment.html')

def contacts(request):
    return render(request, 'service/contacts.html')