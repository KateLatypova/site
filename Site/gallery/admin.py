from django.contrib import admin

from gallery.models import AlbumImage, CommentForImage


class CommentsInLine(admin.StackedInline):
    model = CommentForImage
    fields = ('author', 'text', 'edits', 'created_at', 'updated_at')
    readonly_fields = ('author', 'created_at')
    extra = 0


class AlbumAdmin(admin.ModelAdmin):
    fields = ('name', 'image')
    inlines = [CommentsInLine]
    list_display = ('name',)
    list_editable = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(AlbumImage, AlbumAdmin)