from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заглавие')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    topic = models.ForeignKey('Topic', on_delete=models.PROTECT, verbose_name='Тема')

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = 'Пост'
    #     verbose_name_plural = 'Посты'
    #     ordering = ['-time_created']


class Topic(models.Model):
    name = models.CharField(max_length=200, verbose_name='Тема')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('topic', kwargs={'topic_slug': self.slug})

    # class Meta:
    #     verbose_name = 'Тема'
    #     verbose_name_plural = 'Темы'

