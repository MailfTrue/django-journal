from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Category

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'published_date')
    list_filter = ['published_date','categories']
    search_fields = ['title']
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
