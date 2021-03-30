from django.shortcuts import render, redirect,  get_object_or_404
# from django.http import HttpResponse 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from service.models import Category, Service, Comment
from service.forms import CommentForm
from django.core.paginator import Paginator
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin



# Создаем представление для отображения списка всех категорий (хотя их в проекте только 2)
class CategoryList(ListView):
	model = Category
	context_object_name = 'category_list'

class ServiceList(ListView):
    model = Service
    context_object_name = 'service_list'
    queryset = Service.objects.select_related('category').order_by('-id', '-updated')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.all().order_by('id'),            
        })
        return context

class CategoryServiceList(ListView):
    template_name = 'service/service_list_by_category.html'
    context_object_name = 'object'
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['id'])
        return Service.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'category': get_object_or_404(Category, id=self.kwargs['id'])          
        })
        return context

def comments_view(request):
    comments = Comment.objects.filter(active=True).order_by('-created')
    paginator = Paginator(comments, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request, 'service/comment_list.html', {'form': form})
    else:
        form = CommentForm()

    return render(request, 'service/comment_list.html', {'comments': comments, 'form': form, 'page_obj': page_obj})


class CommentDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'is_staff'
    permission_denied_message = 'Только админ может удалять комментарии, сорян, бро'
    model = Comment
    success_url = reverse_lazy('comments_view')

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
