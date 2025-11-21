from django.contrib import admin
from .models import post, AboutUs


class postAdmin(admin.ModelAdmin):
    list_display = ('title','content', 'img_url', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

# Register your models here.
admin.site.register(post, postAdmin)
admin.site.register(AboutUs)
