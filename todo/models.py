from django.db import models
from django.utils import timezone


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('shopping', 'Shopping'),
        ('health', 'Health'),
        ('learning', 'Learning'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-priority', 'due_date', '-created_at']
    
    def __str__(self):
        return self.title
    
    @property
    def is_overdue(self):
        if self.due_date and not self.completed:
            return timezone.now() > self.due_date
        return False
    
    @property
    def priority_emoji(self):
        priority_emojis = {
            'low': '🟢',
            'medium': '🟡',
            'high': '🟠',
            'urgent': '🔴',
        }
        return priority_emojis.get(self.priority, '🟡')
    
    @property
    def category_emoji(self):
        category_emojis = {
            'work': '💼',
            'personal': '👤',
            'shopping': '🛒',
            'health': '🏥',
            'learning': '📚',
            'other': '📝',
        }
        return category_emojis.get(self.category, '📝')
