# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'proto_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'proto', ['Category'])

        # Adding model 'Page'
        db.create_table(u'proto_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pages', to=orm['proto.Category'])),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=50000)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'proto', ['Page'])

        # Adding model 'PageTab'
        db.create_table(u'proto_pagetab', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children_tabs', to=orm['proto.Page'])),
            ('child', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parent_tabs', to=orm['proto.Page'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'proto', ['PageTab'])

        # Adding model 'Action'
        db.create_table(u'proto_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'proto', ['Action'])

        # Adding M2M table for field applicable_categories on 'Action'
        m2m_table_name = db.shorten_name(u'proto_action_applicable_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('action', models.ForeignKey(orm[u'proto.action'], null=False)),
            ('category', models.ForeignKey(orm[u'proto.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['action_id', 'category_id'])

        # Adding model 'Act'
        db.create_table(u'proto_act', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='acts', to=orm['auth.User'])),
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(related_name='acts', to=orm['proto.Action'])),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='acts', to=orm['proto.Page'])),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'proto', ['Act'])

        # Adding model 'Log'
        db.create_table(u'proto_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('purpose', self.gf('django.db.models.fields.TextField')(max_length=1024)),
            ('act', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['proto.Act'], unique=True, null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'proto', ['Log'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'proto_category')

        # Deleting model 'Page'
        db.delete_table(u'proto_page')

        # Deleting model 'PageTab'
        db.delete_table(u'proto_pagetab')

        # Deleting model 'Action'
        db.delete_table(u'proto_action')

        # Removing M2M table for field applicable_categories on 'Action'
        db.delete_table(db.shorten_name(u'proto_action_applicable_categories'))

        # Deleting model 'Act'
        db.delete_table(u'proto_act')

        # Deleting model 'Log'
        db.delete_table(u'proto_log')


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
        u'proto.act': {
            'Meta': {'object_name': 'Act'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'acts'", 'to': u"orm['proto.Action']"}),
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'acts'", 'to': u"orm['auth.User']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'acts'", 'to': u"orm['proto.Page']"})
        },
        u'proto.action': {
            'Meta': {'object_name': 'Action'},
            'applicable_categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'applicable_actions'", 'symmetrical': 'False', 'to': u"orm['proto.Category']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'proto.category': {
            'Meta': {'object_name': 'Category'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'proto.log': {
            'Meta': {'object_name': 'Log'},
            'act': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['proto.Act']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.TextField', [], {'max_length': '1024'})
        },
        u'proto.page': {
            'Meta': {'object_name': 'Page'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pages'", 'to': u"orm['proto.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '50000'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tab_of': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tabs'", 'to': u"orm['proto.Page']", 'through': u"orm['proto.PageTab']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'proto.pagetab': {
            'Meta': {'object_name': 'PageTab'},
            'child': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parent_tabs'", 'to': u"orm['proto.Page']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children_tabs'", 'to': u"orm['proto.Page']"})
        }
    }

    complete_apps = ['proto']