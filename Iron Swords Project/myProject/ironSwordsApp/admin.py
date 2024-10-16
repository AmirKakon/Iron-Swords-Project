from django.contrib import admin
from .models import Hero, KibbutzStory, NovaPartyTestimony, AbducteeTestimony, Comment, Candle
from django.utils.html import format_html



class HeroAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'hometown', 'country_of_birth', 'hero_story', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return 'No Image'

    image_tag.short_description = 'Image'

admin.site.register(Hero, HeroAdmin)


class KibbutzStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'short_content')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('author', 'created_at')

    def short_content(self, obj):
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content

    short_content.short_description = 'Content'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Show all stories to admins
        if request.user.is_superuser:
            return qs
        # Show only stories created by the user for non-admins
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if not change:  # New object
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None:
            return obj.author == request.user
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None:
            return obj.author == request.user
        return super().has_delete_permission(request, obj)

admin.site.register(KibbutzStory, KibbutzStoryAdmin)


class NovaPartyTestimonyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'story')  # Fields to display in the list view
    search_fields = ('owner', 'story')  # Fields to be searchable

# Register the model with the admin site
admin.site.register(NovaPartyTestimony, NovaPartyTestimonyAdmin)


@admin.register(AbducteeTestimony)
class AbducteeTestimonyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'story', 'author', 'created_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at', 'video_url')  # Fields to display in the list view
    search_fields = ('user__username', 'content')  # Fields to be searchable
    list_filter = ('created_at', 'user')  # Filters for the list view
    ordering = ('-created_at',)  # Order comments by creation date, descending

    def has_delete_permission(self, request, obj=None):
        # Allow deletion if the user is a superuser
        if request.user.is_superuser:
            return True
        # Otherwise, deny deletion permission
        return False

admin.site.register(Comment, CommentAdmin)

class CandleAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'date_lit')
    list_filter = ('date_lit',)
    search_fields = ('name', 'message')

admin.site.register(Candle, CandleAdmin)