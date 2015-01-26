# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SeriesData'
        db.create_table(u'series_seriesdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'series_data', unique=True, to=orm['proto.Page'])),
            ('series_label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('episode_label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('episode_label_plural', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('total_episodes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('aired_episodes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('season_label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('season_label_plural', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('total_seasons', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('aired_seasons', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('season_numbering', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'series', ['SeriesData'])

        # Adding model 'SeasonData'
        db.create_table(u'series_seasondata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'season_data', unique=True, to=orm['proto.Page'])),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'seasons', to=orm['series.SeriesData'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'series', ['SeasonData'])

        # Adding model 'EpisodeData'
        db.create_table(u'series_episodedata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'episode_data', unique=True, to=orm['proto.Page'])),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'episodes', to=orm['series.SeriesData'])),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'episodes', to=orm['series.SeasonData'])),
            ('number_in_series', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('number_in_season', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'series', ['EpisodeData'])


    def backwards(self, orm):
        # Deleting model 'SeriesData'
        db.delete_table(u'series_seriesdata')

        # Deleting model 'SeasonData'
        db.delete_table(u'series_seasondata')

        # Deleting model 'EpisodeData'
        db.delete_table(u'series_episodedata')


    models = {
        u'proto.page': {
            'Meta': {'object_name': 'Page'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'page_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'series.episodedata': {
            'Meta': {'ordering': "[u'-date_added']", 'object_name': 'EpisodeData'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number_in_season': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'number_in_series': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'page': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'episode_data'", 'unique': 'True', 'to': u"orm['proto.Page']"}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'episodes'", 'to': u"orm['series.SeasonData']"}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'episodes'", 'to': u"orm['series.SeriesData']"})
        },
        u'series.seasondata': {
            'Meta': {'ordering': "[u'-date_added']", 'object_name': 'SeasonData'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'page': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'season_data'", 'unique': 'True', 'to': u"orm['proto.Page']"}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'seasons'", 'to': u"orm['series.SeriesData']"})
        },
        u'series.seriesdata': {
            'Meta': {'ordering': "[u'-date_added']", 'object_name': 'SeriesData'},
            'aired_episodes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'aired_seasons': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'episode_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'episode_label_plural': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'series_data'", 'unique': 'True', 'to': u"orm['proto.Page']"}),
            'season_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'season_label_plural': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'season_numbering': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'series_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_episodes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_seasons': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['series']