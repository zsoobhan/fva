from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$',
        views.YoutubeVideoListView.as_view(), name="youtube-list-view"),
    url(r'^(?P<slug>[-_\w]+)/$',
        views.YoutubeEntryDetailView .as_view(), name='youtube-detail-view'),
)
