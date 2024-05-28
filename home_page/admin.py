from django.contrib import admin
from .models import BlogPost, Comment, Tag
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'author', 'published_date', 'status')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    summernote_fields = ('content', 'tags', 'benefits', 'ingredients', 'how_to_use')

# Register your models here.

admin.site.register(Comment)
admin.site.register(Tag)
