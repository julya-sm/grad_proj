from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField, SearchVector
from django.db.models.signals import post_save
from django.dispatch import receiver


class ViewCount(models.Model):
    ipaddress = models.GenericIPAddressField(blank=True, null=True, verbose_name='IP адрес')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заглавие')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Лого темы')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    topic = models.ForeignKey('Topic', on_delete=models.PROTECT, verbose_name='Тема')
    viewers = models.ManyToManyField(ViewCount, blank=True, verbose_name='Просмотры')
    search_vector = SearchVectorField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-time_created']
        indexes = [GinIndex(fields=["search_vector"])]

    def update_search_vector(self):
        qs = Blog.objects.filter(pk=self.pk)
        qs.update(search_vector=SearchVector('title', 'content'))


@receiver(post_save, sender=Blog)
def post_save_blogpost(sender, instance, created, update_fields, **kwargs):
    instance.update_search_vector()


class Topic(models.Model):
    name = models.CharField(max_length=200, verbose_name='Тема')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('top', kwargs={'top_slug': self.slug})

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
