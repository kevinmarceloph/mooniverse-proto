from __future__ import unicode_literals
from datetime import datetime
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class SeriesData(models.Model):
    page = models.OneToOneField('proto.Page', related_name='series_data', limit_choices_to={'page_type': 'series'})

    series_label = models.CharField(max_length=100)

    episode_label = models.CharField(max_length=100)
    episode_label_plural = models.CharField(max_length=100)
    total_episodes = models.IntegerField(default=0)
    aired_episodes = models.IntegerField(default=0)

    season_label = models.CharField(max_length=100)
    season_label_plural = models.CharField(max_length=100)
    total_seasons = models.IntegerField(default=0)
    aired_seasons = models.IntegerField(default=0)

    season_numbering = models.BooleanField(default=False)

    date_added = models.DateTimeField(default=datetime.now)
    date_edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return str(self.page)


@python_2_unicode_compatible
class SeasonData(models.Model):
    page = models.OneToOneField('proto.Page', related_name='season_data', limit_choices_to={'page_type': 'season'})
    series = models.ForeignKey(SeriesData, related_name='seasons')

    number = models.IntegerField(default=0)

    date_added = models.DateTimeField(default=datetime.now)
    date_edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    @property
    def numbering(self):
        return '{} {}'.format(self.series.season_label.title(), self.number)

    def __str__(self):
        return str(self.page)


@python_2_unicode_compatible
class EpisodeData(models.Model):
    page = models.OneToOneField('proto.Page', related_name='episode_data', limit_choices_to={'page_type': 'episode'})
    series = models.ForeignKey(SeriesData, related_name='episodes')
    season = models.ForeignKey(SeasonData, related_name='episodes')

    number_in_series = models.IntegerField(default=0)
    number_in_season = models.IntegerField(default=0)
    name = models.CharField(max_length=100)

    date_added = models.DateTimeField(default=datetime.now)
    date_edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    @property
    def numbering(self):
        if self.series.season_numbering:
            return '{}, {} {}'.format(self.season.numbering, self.series.episode_label.title(), self.number_in_season)
        else:
            return '{} {}'.format(self.series.episode_label.title(), self.number_in_series)

    def __str__(self):
        return str(self.page)
