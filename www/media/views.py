from django.views import generic
from django.http import Http404

from . import models


class BaseEntryListView(generic.ListView):
    context_object_name = 'active_objects'
    paginate_by = 10

    def get_queryset(self):
        'return the active entries'
        queryset = super(BaseEntryListView, self).get_queryset()
        return [entry for entry in queryset if entry.is_active]


class BaseEntryDetailView(generic.DetailView):

    def get_object(self):
        obj = super(BaseEntryDetailView, self).get_object()
        user = getattr(self.request, 'user')

        # return early if superuser
        if user and user.is_superuser:
            return obj

        if not obj.is_active:
            raise Http404('The object requested is currently inactive.')

        return obj


class YoutubeVideoListView(BaseEntryListView):
    model = models.YoutubeVideo
    template_name = 'media/youtubelist.html'
    queryset = models.YoutubeVideo.objects.filter(status=models.PUBLISHED)
    queryset = queryset.prefetch_related('tags')


class YoutubeEntryDetailView(generic.DetailView):
    template_name = 'media/youtubedetail.html'
    model = models.YoutubeVideo
