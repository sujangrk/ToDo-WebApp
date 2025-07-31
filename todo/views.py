from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from django.http import HttpResponse
from datetime import datetime
import csv
from .models import Task
from .forms import TaskForm


def task_list(request):
    """Main view for displaying and filtering tasks"""
    tasks = Task.objects.all()
    
    # Filtering
    filter_completed = request.GET.get('filter')
    if filter_completed == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_completed == 'pending':
        tasks = tasks.filter(completed=False)
    
    # Category filter
    category_filter = request.GET.get('category')
    if category_filter:
        tasks = tasks.filter(category=category_filter)
    
    # Priority filter
    priority_filter = request.GET.get('priority')
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Sort options
    sort_by = request.GET.get('sort', 'priority')
    if sort_by == 'due_date':
        tasks = tasks.order_by('due_date', '-created_at')
    elif sort_by == 'created':
        tasks = tasks.order_by('-created_at')
    elif sort_by == 'title':
        tasks = tasks.order_by('title')
    else:
        tasks = tasks.order_by('-priority', 'due_date', '-created_at')
    
    # Calculate statistics
    pending_count = Task.objects.filter(completed=False).count()
    completed_count = Task.objects.filter(completed=True).count()
    urgent_count = Task.objects.filter(priority='urgent').count()
    
    context = {
        'tasks': tasks,
        'categories': Task.CATEGORY_CHOICES,
        'priorities': Task.PRIORITY_CHOICES,
        'current_filter': filter_completed,
        'current_category': category_filter,
        'current_priority': priority_filter,
        'current_sort': sort_by,
        'search_query': search_query,
        'pending_count': pending_count,
        'completed_count': completed_count,
        'urgent_count': urgent_count,
    }
    
    return render(request, 'todo/task_list.html', context)


def task_create(request):
    """Create a new task"""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'Task "{task.title}" created successfully!')
            return redirect('todo:task_list')
    else:
        form = TaskForm()
    
    return render(request, 'todo/task_form.html', {'form': form, 'action': 'Create'})


def task_update(request, pk):
    """Update an existing task"""
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'Task "{task.title}" updated successfully!')
            return redirect('todo:task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'todo/task_form.html', {
        'form': form, 
        'task': task, 
        'action': 'Update'
    })


def task_delete(request, pk):
    """Delete a task"""
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        task_title = task.title
        task.delete()
        messages.success(request, f'Task "{task_title}" deleted successfully!')
        return redirect('todo:task_list')
    
    return render(request, 'todo/task_confirm_delete.html', {'task': task})


def task_toggle(request, pk):
    """Toggle task completion status"""
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    
    status = "completed" if task.completed else "marked as pending"
    messages.success(request, f'Task "{task.title}" {status}!')
    
    return redirect('todo:task_list')


def task_bulk_action(request):
    """Handle bulk actions on tasks"""
    if request.method == 'POST':
        action = request.POST.get('action')
        task_ids = request.POST.getlist('task_ids')
        
        if action and task_ids:
            tasks = Task.objects.filter(id__in=task_ids)
            
            if action == 'complete':
                tasks.update(completed=True)
                messages.success(request, f'{len(tasks)} tasks marked as completed!')
            elif action == 'delete':
                count = len(tasks)
                tasks.delete()
                messages.success(request, f'{count} tasks deleted successfully!')
    
    return redirect('todo:task_list')


def export_tasks_csv(request):
    """Export tasks to CSV format"""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tasks.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Title', 'Description', 'Status', 'Priority', 'Category', 'Due Date', 'Created At'])
    
    tasks = Task.objects.all()
    for task in tasks:
        status = 'Completed' if task.completed else 'Pending'
        due_date = task.due_date.strftime('%Y-%m-%d %H:%M') if task.due_date else 'No due date'
        created_at = task.created_at.strftime('%Y-%m-%d %H:%M')
        
        writer.writerow([
            task.title,
            task.description or '',
            status,
            task.get_priority_display(),
            task.get_category_display(),
            due_date,
            created_at
        ])
    
    return response


def task_statistics(request):
    """Display detailed task statistics and analytics"""
    from django.db.models import Count, Q
    from datetime import timedelta
    
    # Basic counts
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(completed=True).count()
    pending_tasks = Task.objects.filter(completed=False).count()
    overdue_tasks = Task.objects.filter(
        Q(due_date__lt=timezone.now()) & Q(completed=False)
    ).count()
    
    # Completion rate
    completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    
    # Priority distribution
    priority_stats = Task.objects.values('priority').annotate(count=Count('priority'))
    priority_data = {item['priority']: item['count'] for item in priority_stats}
    
    # Category distribution
    category_stats = Task.objects.values('category').annotate(count=Count('category'))
    category_data = {item['category']: item['count'] for item in category_stats}
    
    # Recent activity (last 7 days)
    week_ago = timezone.now() - timedelta(days=7)
    recent_tasks = Task.objects.filter(created_at__gte=week_ago).count()
    
    # Tasks by status and priority
    urgent_pending = Task.objects.filter(priority='urgent', completed=False).count()
    high_pending = Task.objects.filter(priority='high', completed=False).count()
    
    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_tasks': overdue_tasks,
        'completion_rate': round(completion_rate, 1),
        'priority_data': priority_data,
        'category_data': category_data,
        'recent_tasks': recent_tasks,
        'urgent_pending': urgent_pending,
        'high_pending': high_pending,
    }
    
    return render(request, 'todo/task_statistics.html', context)


def quick_search(request):
    """Quick search for tasks with AJAX support"""
    query = request.GET.get('q', '')
    if not query:
        return redirect('todo:task_list')
    
    tasks = Task.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(category__icontains=query) |
        Q(priority__icontains=query)
    ).order_by('-priority', 'due_date', '-created_at')
    
    context = {
        'tasks': tasks,
        'search_query': query,
        'results_count': tasks.count(),
    }
    
    return render(request, 'todo/quick_search.html', context)
