from django.contrib import admin
from django.conf import settings

from perms.admin import TendenciBaseModelAdmin
from models import Video, Category
from forms import VideoForm

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

class VideoAdmin(TendenciBaseModelAdmin):

    list_display = ['title', 'category', 'ordering']
    list_filter = ['category']
    list_editable = ['ordering']
    prepopulated_fields = {'slug': ['title']}
    search_fields = ['question','answer']
    fieldsets = (
        (None, {'fields': ('title','slug','category','image','video_url','tags','description')}),
        ('Permissions', {'fields': ('allow_anonymous_view',)}),
        ('Advanced Permissions', {'classes': ('collapse',),'fields': (
            'user_perms',
            'member_perms',
            'group_perms',
        )}),
        ('Publishing Status', {'fields': (
            'status',
            'status_detail'
        )}),
    )
    form = VideoForm
    ordering = ['-ordering']

    class Media:
        js = (
            '%sjs/global/tinymce.event_handlers.js' % settings.STATIC_URL,
            '%sjs/jquery-1.6.2.min.js' % settings.STATIC_URL,
            '%sjs/jquery-ui-1.8.17.custom.min.js' % settings.STATIC_URL,
            '%sjs/admin/admin-list-reorder.js' % settings.STATIC_URL,
        )

admin.site.register(Video, VideoAdmin)
admin.site.register(Category, CategoryAdmin)