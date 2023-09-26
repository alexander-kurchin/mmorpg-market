from django.contrib import admin

from .models import AdvertModel, ReplyModel


class AdvertModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'category', 'title', 'created_at', 'has_accepted_reply',)
    search_fields = ('title', 'content',)
    list_filter = ('user', 'created_at', 'category',)


class ReplyModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'advert', 'text', 'created_at',)
    search_fields = ('text',)
    list_filter = ('user', 'advert',)


admin.site.register(AdvertModel, AdvertModelAdmin)
admin.site.register(ReplyModel, ReplyModelAdmin)
