from __future__ import unicode_literals
from datetime import datetime
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django_extensions.db.fields.json import JSONField


@python_2_unicode_compatible
class Page(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    page_type = models.CharField(max_length=100)
    short_description = models.TextField(blank=True)
    data = JSONField(blank=True)

    date_added = models.DateTimeField(default=datetime.now)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Image(models.Model):
    image = models.ImageField(upload_to='images', height_field='height', width_field='width')
    height = models.SmallIntegerField(default=0)
    width = models.SmallIntegerField(default=0)

    date_added = models.DateTimeField(default=datetime.now)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.name


@python_2_unicode_compatible
class PageImage(models.Model):
    page = models.ForeignKey(Page, related_name='page_images')
    image = models.ForeignKey(Image, related_name='page_images')
    order = models.SmallIntegerField(default=0)

    date_added = models.DateTimeField(default=datetime.now)
    date_edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{} / {}'.format(self.page, self.image)


@python_2_unicode_compatible
class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updates')
    text = models.TextField(max_length=1024)

    date_added = models.DateTimeField(default=datetime.now)
    date_edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '{}: {}'.format(self.user, self.text)

    def render_text(self):
        parts = []

        remaining = self.text
        pointer = 0
        for mention in self.mentions.all().order_by('start'):
            if mention.start is not None and mention.end is not None:
                parts.append(remaining[:mention.start - pointer])
                link_text = remaining[mention.start - pointer:mention.end - pointer]
                link = '<a href="{}">{}</a>'.format(reverse('page_view', args=[mention.page.slug]), link_text)
                parts.append(link)
                remaining = remaining[mention.end - pointer:]
                pointer += mention.end - pointer
                print remaining, pointer
        parts.append(remaining)
        return ''.join(parts)


@python_2_unicode_compatible
class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ratings')
    page = models.ForeignKey(Page, related_name='ratings')
    rating = models.SmallIntegerField()

    date_added = models.DateTimeField(default=datetime.now)
    date_edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '{} / {}: {}'.format(self.user, self.page, self.rating)


@python_2_unicode_compatible
class Mention(models.Model):
    update = models.ForeignKey(Update, related_name='mentions')
    page = models.ForeignKey(Page, related_name='mentions')
    start = models.PositiveIntegerField(blank=True, null=True)
    end = models.PositiveIntegerField(blank=True, null=True)

    date_added = models.DateTimeField(default=datetime.now)
    date_edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '#{}: {}'.format(self.update_id, self.page)
