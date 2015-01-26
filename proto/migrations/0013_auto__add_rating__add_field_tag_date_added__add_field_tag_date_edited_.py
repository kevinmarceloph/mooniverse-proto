# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rating'
        db.create_table(u'proto_rating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ratings', to=orm['auth.User'])),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ratings', to=orm['proto.Page'])),
            ('rating', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'proto', ['Rating'])

        # Adding field 'Tag.date_added'
        db.add_column(u'proto_tag', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Tag.date_edited'
        db.add_column(u'proto_tag', 'date_edited',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 11, 26, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Tab.date_added'
        db.add_column(u'proto_tab', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Tab.date_edited'
        db.add_column(u'proto_tab', 'date_edited',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 11, 26, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'PageTag.date_added'
        db.add_column(u'proto_pagetag', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'PageTag.date_edited'
        db.add_column(u'proto_pagetag', 'date_edited',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 11, 26, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'PageImage.date_added'
        db.add_column(u'proto_pageimage', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'PageImage.date_edited'
        db.add_column(u'proto_pageimage', 'date_edited',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 11, 26, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Page.date_added'
        db.add_column(u'proto_page', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Page.date_edited'
        db.add_column(u'proto_page', 'date_edited',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 11, 26, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Image.date_added'
        db.add_column(u'proto_image', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Image.date_edited'
        db.add_column(u'proto_image', 'date_edited',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 11, 26, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Rating'
        db.delete_table(u'proto_rating')

        # Deleting field 'Tag.date_added'
        db.delete_column(u'proto_tag', 'date_added')

        # Deleting field 'Tag.date_edited'
        db.delete_column(u'proto_tag', 'date_edited')

        # Deleting field 'Tab.date_added'
        db.delete_column(u'proto_tab', 'date_added')

        # Deleting field 'Tab.date_edited'
        db.delete_column(u'proto_tab', 'date_edited')

        # Deleting field 'PageTag.date_added'
        db.delete_column(u'proto_pagetag', 'date_added')

        # Deleting field 'PageTag.date_edited'
        db.delete_column(u'proto_pagetag', 'date_edited')

        # Deleting field 'PageImage.date_added'
        db.delete_column(u'proto_pageimage', 'date_added')

        # Deleting field 'PageImage.date_edited'
        db.delete_column(u'proto_pageimage', 'date_edited')

        # Deleting field 'Page.date_added'
        db.delete_column(u'proto_page', 'date_added')

        # Deleting field 'Page.date_edited'
        db.delete_column(u'proto_page', 'date_edited')

        # Deleting field 'Image.date_added'
        db.delete_column(u'proto_image', 'date_added')

        # Deleting field 'Image.date_edited'
        db.delete_column(u'proto_image', 'date_edited')


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