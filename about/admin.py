from django.contrib import admin
from .models import About, Feedback, Issues
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'content', 'order',)
    search_fields = ['title', 'content', 'order']
    list_filter = ('title', 'content', 'order')


admin.site.register(Issues, admin.ModelAdmin)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('issue', 'email', 'message', 'read',)
    search_fields = ['issue', 'email', 'message']
    list_filter = ('issue', 'email', 'read')
    