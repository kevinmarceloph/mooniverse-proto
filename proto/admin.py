from django.contrib import admin
from .models import Page, Image, PageImage, Update, Mention


admin.site.register(Page)
admin.site.register(Image)
admin.site.register(PageImage)
admin.site.register(Update)
admin.site.register(Mention)
