from django.contrib import admin

from news.models import NewsCategory, News, Tags, Ads

admin.site.register(NewsCategory)
admin.site.register(Tags)

class NewsAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(News, NewsAdmin)

admin.site.register(Ads)
