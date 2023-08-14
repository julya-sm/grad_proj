from .models import *
from django.db.models import Count


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        topics = Topic.objects.annotate(Count('blog'))

        context['topics'] = topics

        if 'topic_selected' not in context:
            context['topic_selected'] = 0
        return context
