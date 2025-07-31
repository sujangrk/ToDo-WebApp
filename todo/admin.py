from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'category', 'completed', 'due_date', 'created_at']
    list_filter = ['completed', 'priority', 'category', 'created_at', 'due_date']
    search_fields = ['title', 'description']
    list_editable = ['completed', 'priority', 'category']
    date_hierarchy = 'created_at'
    ordering = ['-priority', 'due_date', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description')
        }),
        ('Status & Priority', {
            'fields': ('completed', 'priority', 'category')
        }),
        ('Timing', {
            'fields': ('due_date', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
    
    def get_list_display(self, request):
        list_display = list(super().get_list_display(request))
        if 'priority' in list_display:
            list_display.insert(list_display.index('priority'), 'priority_emoji')
        if 'category' in list_display:
            list_display.insert(list_display.index('category'), 'category_emoji')
        return list_display
    
    def priority_emoji(self, obj):
        return obj.priority_emoji
    priority_emoji.short_description = 'Priority'
    
    def category_emoji(self, obj):
        return obj.category_emoji
    category_emoji.short_description = 'Category'
