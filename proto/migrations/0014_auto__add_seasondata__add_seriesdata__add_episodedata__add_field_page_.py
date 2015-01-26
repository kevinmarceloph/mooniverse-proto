# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SeasonData'
        db.create_table(u'proto_seasondata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'season_data', unique=True, to=orm['proto.Page'])),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'seasons', to=orm['proto.SeriesData'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'proto', ['SeasonData'])

        # Adding model 'SeriesData'
        db.create_table(u'proto_seriesdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'series_data', unique=True, to=orm['proto.Page'])),
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
        db.send_create_signal(u'proto', ['SeriesData'])

        # Adding model 'EpisodeData'
        db.create_table(u'proto_episodedata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'episode_data', unique=True, to=orm['proto.Page'])),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'episodes', to=orm['proto.SeriesData'])),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'episodes', to=orm['proto.SeasonData'])),
            ('number_in_series', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('number_in_season', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'proto', ['EpisodeData'])

        # Adding field 'Page.page_type'
        db.add_column(u'proto_page', 'page_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'SeasonData'
        db.delete_table(u'proto_seasondata')

        # Deleting model 'SeriesData'
        db.delete_table(u'proto_seriesdata')

        # Deleting model 'EpisodeData'
        db.delete_table(u'proto_episodedata')

        # Deleting field 'Page.page_type'
        db.delete_column(u'proto_page', 'page_type')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'proto.episodedata': {
            'Meta': {'ordering': "[u'-date_added']", 'object_name': 'EpisodeData'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number_in_season': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'number_in_series': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'page': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'episode_data'", 'unique': 'True', 'to': u"orm['proto.Page']"}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'episodes'", 'to': u"orm['proto.SeasonData']"}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'episodes'", 'to': u"orm['proto.SeriesData']"})
        },
        u'proto.image': {
            'Meta': {'object_name': 'Image'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'width': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
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
        u'proto.pageimage': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'PageImage'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'page_images'", 'to': u"orm['proto.Image']"}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'page_images'", 'to': u"orm['proto.Page']"})
        },
        u'proto.pagetag': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'PageTag'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_class': ('django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '10'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'page_tags'", 'to': u"orm['proto.Page']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'page_tags'", 'to': u"orm['proto.Tag']"})
        },
        u'proto.rating': {
            'Meta': {'ordering': "[u'-date_added']", 'object_name': 'Rating'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ratings'", 'to': u"orm['proto.Page']"}),
            'rating': ('django.db.models.fields.SmallIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ratings'", 'to': u"orm['auth.User']"})
        },
        u'proto.seasondata': {
            'Meta': {'ordering': "[u'-date_added']", 'object_name': 'SeasonData'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'page': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'season_data'", 'unique': 'True', 'to': u"orm['proto.Page']"}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'seasons'", 'to': u"orm['proto.SeriesData']"})
        },
        u'proto.seriesdata': {
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
            'total_episodes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_seasons': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'proto.tab': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'Tab'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'tabs'", 'to': u"orm['proto.Page']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'proto.tag': {
            'Meta': {'object_name': 'Tag'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'proto.update': {
            'Meta': {'ordering': "[u'-date_added']", 'object_name': 'Update'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'updates'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['proto']