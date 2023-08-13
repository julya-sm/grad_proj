from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *
from django.urls import reverse_lazy


class BlogHome(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['topic_selected'] = 0
        return context

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).select_related('topic')


class ShowPost(DetailView):
    model = Blog
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context


class BlogTopic(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Blog.objects.filter(topic__slug=self.kwargs['top_slug'], is_published=True).select_related('topic')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Тема - ' + str(context['posts'][0].topic)
        context['topic_selected'] = context['posts'][0].topic_id
        return context


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'blog/add_page.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context
