from django.contrib import admin
from .models import Posts



class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","timestamp","updated"]
    list_display_links = ["updated"]
    list_filter = ["updated","timestamp"]
    search_fields = ["title","content"]
    list_editable = ["title"]
    class Meta:
        model=Posts
admin.site.register(Posts,PostModelAdmin)
