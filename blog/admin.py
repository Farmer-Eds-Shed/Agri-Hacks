from django.contrib import admin
from .models import Post
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content', 'author']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('document', 'concept')
