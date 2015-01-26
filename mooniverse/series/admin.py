from django.contrib import admin
from .models import SeriesData, SeasonData, EpisodeData


admin.site.register(SeriesData)
admin.site.register(SeasonData)
admin.site.register(EpisodeData)
