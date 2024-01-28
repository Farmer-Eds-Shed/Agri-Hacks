from django.contrib import admin
from .models import Post
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('document','concept')