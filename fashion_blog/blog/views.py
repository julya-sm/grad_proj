from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogHome(DataMixin, ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        t_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(t_def.items()))

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).select_related('topic')


class ShowPost(DataMixin, DetailView):
    model = Blog
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        t_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(t_def.items()))


class BlogTopic(DataMixin, ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Blog.objects.filter(topic__slug=self.kwargs['top_slug'], is_published=True).select_related('topic')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        t = Topic.objects.get(slug=self.kwargs['top_slug'])
        t_def = self.get_user_context(title=str(t.name), topic_selected=t.pk)
        return dict(list(context.items()) + list(t_def.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/add_page.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        t_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(t_def.items()))
