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
    template_name = 'media/youtube_list.html'
    queryset = models.YoutubeVideo.objects.filter(status=models.PUBLISHED)
    queryset = queryset.prefetch_related('tags')


class FlickrAlbumListView(BaseEntryListView):
    model = models.FlickrAlbum
    template_name = 'media/flickr_list.html'
    queryset = models.FlickrAlbum.objects.filter(status=models.PUBLISHED)
    queryset = queryset.prefetch_related('tags')


class YoutubeEntryDetailView(BaseEntryDetailView):
    model = models.YoutubeVideo
    template_name = 'media/youtube_detail.html'


class FlickAlbumDetailView(BaseEntryDetailView):
    model = models.FlickrAlbum
    template_name = 'media/flickr_detail.html'


class PressListView(BaseEntryListView):
    model = models.PressEntry
    template_name = 'media/press_list.html'


class PressDetailView(BaseEntryDetailView):
    model = models.PressEntry
    template_name = 'media/press_detail.html'


class TagListView(BaseEntryListView):
    model = models.Tag
    template_name = 'media/tag_list.html'


class TagDetailView(BaseEntryDetailView):
    model = models.Tag
    template_name = 'media/tag_detail.html'
