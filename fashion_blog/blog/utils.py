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


class ViewCountMixin:
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if hasattr(self.object, 'viewers'):
            viewer, created = ViewCount.objects.get_or_create(
                ipaddress=None if request.user.is_authenticated else get_client_ip(request),
                user=request.user if request.user.is_authenticated else None
            )
            if self.object.viewers.filter(id=viewer.id).count() == 0:
                self.object.viewers.add(viewer)
        return response


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
