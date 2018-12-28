from ckeditor.fields import RichTextField
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db import models

from . import FA_CHOICES


PUBLISHED = 'PUBLISHED'
DRAFT = 'DRAFT'
STATUS_CHOICES = [
    (PUBLISHED, 'Published'),
    (DRAFT, 'Draft')
]

RELATED_NAMES = ['youtube_entries', 'flickr_entries', 'press_entries']


class Tag(models.Model):
    title = models.CharField(max_length=4096)
    slug = models.SlugField(max_length=4096, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    blurb = RichTextField(blank=True)

    def __unicode__(self):
        return u'{slug}'.format(slug=self.slug)

    def _filter_for_active_entries(self, related_name):
        return [
            entry for entry in getattr(self, related_name).all()
            if entry.is_active
        ]

    @property
    def is_active(self):
        'Returns a boolean if tag contains active content'
        return any(self.active_content())

    def get_absolute_url(self):
        return reverse(
            'media:tag-detail-view', kwargs={'slug': self.slug}
        )

    def active_content(self):
        active_content = []
        for related_name in RELATED_NAMES:
            active_content += self._filter_for_active_entries(related_name)
        return active_content

    @property
    def get_ga_label(self):
        return 'tag-{slug}-{id}'.format(slug=self.slug[:10], id=self.id)

    class Meta:
        get_latest_by = 'date_created'
        ordering = ['-date_created']


class AbstractMediaEntry(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(null=True, blank=True, db_index=True)
    date = models.DateField(
        null=True,
        blank=True,
        help_text='The date visible on the post')
    status = models.CharField(
        max_length='16',
        help_text='The status of the object',
        choices=STATUS_CHOICES,
        default=DRAFT)
    title = models.CharField(max_length=4096)
    slug = models.SlugField(max_length=4096, unique=True)
    subtitle = models.CharField(blank=True, max_length=4096)
    content = RichTextField(blank=True)
    meta_description = models.TextField(blank=True, max_length=1024)
    icon = models.CharField(
        max_length=64,
        help_text='The font awesome icon to be displayed',
        default='fa-align-right',
        choices=FA_CHOICES
    )

    class Meta:
        abstract = True
        get_latest_by = 'date_published'
        ordering = ['-date_published']

    def __unicode__(self):
        return u'{slug}'.format(slug=self.slug)

    @property
    def is_active(self):
        published_now = False
        conditions = [self.status == PUBLISHED]
        if self.date_published:
            published_now = self.date_published <= timezone.now()
        conditions.append(published_now)
        return all(conditions)

    def media_prefix(self):
        return 'media'

    def default_icon(self):
        return 'fa-{prefix}'.format(prefix=self.media_prefix())

    @property
    def get_ga_label(self):
        return '{pre}-{slug}-{id}'.format(
            pre=self.media_prefix(), slug=self.slug[:10], id=self.id)


class PressEntry(AbstractMediaEntry):

    external_url = models.CharField(
        max_length=2000,
        help_text='The full external url e.g. https://www.google.co.uk',
        blank=True
    )
    tags = models.ManyToManyField(Tag, related_name='press_entries')

    def get_absolute_url(self):
        return reverse(
            'media:press-detail-view', kwargs={'slug': self.slug}
        )

    class Meta:
        get_latest_by = 'date_published'
        ordering = ['-date_published']
        verbose_name = 'Press Entry'
        verbose_name_plural = 'Press Entries'

    def media_prefix(self):
        return 'newspaper-o'


class YoutubeVideo(AbstractMediaEntry):
    youtube_id = models.CharField(
        max_length=16, help_text='The YouTube ID of the video.')
    tags = models.ManyToManyField(Tag, related_name='youtube_entries')

    def get_absolute_url(self):
        return reverse(
            'media:youtube-detail-view', kwargs={'slug': self.slug}
        )

    class Meta:
        get_latest_by = 'date_published'
        ordering = ['-date_published']
        verbose_name = 'Youtube Video'
        verbose_name_plural = 'Youtube Videos'

    def media_prefix(self):
        return 'youtube'


class FlickrAlbum(AbstractMediaEntry):
    tags = models.ManyToManyField(Tag, related_name='flickr_entries')
    flickr_album_url = models.CharField(
        max_length=1024,
        help_text='Flickr album url'
    )
    flickr_thumbnail_url = models.CharField(
        max_length=1024,
        help_text='looks like https://farm2.staticflickr.com'
                  '/1907/43656216960_4a56163a49_m.jpg'
    )

    def get_absolute_url(self):
        return reverse('media:flickr-detail-view', kwargs={'slug': self.slug})

    class Meta:
        get_latest_by = 'date_published'
        ordering = ['-date_published']
        verbose_name = 'Flickr Album'
        verbose_name_plural = 'Flickr Albums'

    def media_prefix(self):
        return 'flickr'
