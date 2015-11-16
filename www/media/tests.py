import factory
import datetime

from django.utils import timezone
from django.test import TestCase

from . import models


class YoutubeEntryTests(TestCase):

    def setUp(self):
        self.youtube_entry = YoutubeEntryFactory.create()

    def test_youtube_is_active_published_past(self):
        self.youtube_entry.date_published = past()
        self.youtube_entry.save()

        self.assertTrue(self.youtube_entry.is_active)

    def test_youtube_is_inactive_published_future(self):
        self.youtube_entry.date_published = future()
        self.youtube_entry.save()

        self.assertFalse(self.youtube_entry.is_active)

    def test_youtube_is_inactive_published_not_published(self):
        self.youtube_entry.date_published = past()
        self.youtube_entry.status = models.DRAFT
        self.youtube_entry.save()

        self.assertFalse(self.youtube_entry.is_active)

    def test_youtube_is_inactive_published_no_date_published(self):
        self.youtube_entry.date_published = None
        self.youtube_entry.status = models.PUBLISHED
        self.youtube_entry.save()

        self.assertFalse(self.youtube_entry.is_active)


# Test Utils
class YoutubeEntryFactory(factory.django.DjangoModelFactory):
    status = models.PUBLISHED
    title = 'This is a test title'
    subtitle = 'This is a test subtitle'
    content = 'The quick brown fox jumps over the lazy dog. '*10
    slug = factory.Sequence(lambda n: "slug-%03d" % n)

    class Meta:
        model = models.youtubeEntry


def past():
    return timezone.now() - datetime.timedelta(days=1)


def future():
    return timezone.now() + datetime.timedelta(days=1)
