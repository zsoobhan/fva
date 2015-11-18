from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^videos/$',
        views.YoutubeVideoListView.as_view(), name="youtube-list-view"),
    url(r'^tags/$',
        views.TagListView.as_view(), name='tag-list-view'),
    url(r'^videos/(?P<slug>[-_\w]+)/$',
        views.YoutubeEntryDetailView .as_view(), name='youtube-detail-view'),
    url(r'^tags/(?P<slug>[-_\w]+)/$',
        views.TagDetailView.as_view(), name='tag-detail-view'),
)
