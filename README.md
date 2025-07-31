# DevTask Tracker - Django To-Do Application

A modern, feature-rich to-do application built with Django for developers who need to track their chaos before it tracks them.

## 🚀 Features

### Core Features
- ✅ **Add new tasks** with title, description, priority, category, and due date
- ✅ **Mark tasks as complete/incomplete** with one-click toggle
- ✅ **Delete tasks** with confirmation dialog
- ✅ **Persistent storage** using SQLite database
- ✅ **Modern, responsive UI** with Bootstrap 5 and custom styling

### Advanced Features
- 🎯 **Priority levels** with emoji indicators (Urgent 🔴, High 🟠, Medium 🟡, Low 🟢)
- 📂 **Categories** with emoji icons (Work 💼, Personal 👤, Shopping 🛒, Health 🏥, Learning 📚, Other 📝)
- 📅 **Due dates** with overdue detection
- 🔍 **Advanced search functionality** with dedicated results page
- 🎛️ **Advanced filtering** by status, category, and priority
- 📊 **Sorting options** by priority, due date, creation date, or title
- 📦 **Bulk actions** for completing or deleting multiple tasks
- 📈 **Comprehensive statistics dashboard** with analytics and insights
- 📤 **CSV export functionality** for data portability
- 🎨 **Dark mode aesthetic** with gradient backgrounds and glass-morphism effects

## 🛠️ Tech Stack

- **Backend**: Django 5.2.3
- **Database**: SQLite3
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Styling**: Custom CSS with modern design patterns
- **Python**: 3.13.1

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone or Download
```bash
# If you have this as a git repository
git clone <repository-url>
cd todo-app

# Or if you're working with the files directly
cd todo-app
```

### Step 2: Install Dependencies
```bash
pip install django
```

### Step 3: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create Admin User (Optional)
```bash
python manage.py createsuperuser
```

### Step 5: Run the Development Server
```bash
python manage.py runserver
```

### Step 6: Access the Application
- **Main Application**: http://127.0.0.1:8000/
- **Admin Interface**: http://127.0.0.1:8000/admin/

## 🎯 Usage Guide

### Creating Tasks
1. Click the "New Task" button or the floating "+" button
2. Fill in the task details:
   - **Title** (required): Brief description of the task
   - **Description** (optional): Detailed information
   - **Priority**: Choose from Low to Urgent
   - **Category**: Organize tasks by type
   - **Due Date**: Set deadlines (optional)

### Managing Tasks
- **Complete/Incomplete**: Click the checkmark button to toggle status
- **Edit**: Click the pencil icon to modify task details
- **Delete**: Click the trash icon to remove tasks
- **Bulk Actions**: Select multiple tasks and apply actions

### Filtering & Searching
- **Search**: Use the search box to find tasks by title, description, category, or priority
- **Quick Search**: Access dedicated search page for advanced filtering
- **Status Filter**: Show all, pending, or completed tasks
- **Category Filter**: Filter by task category
- **Priority Filter**: Show tasks by priority level
- **Sort**: Arrange tasks by priority, due date, creation date, or title

### Analytics & Export
- **Statistics Dashboard**: View detailed analytics including completion rates, priority distribution, and overdue tasks
- **CSV Export**: Download all task data in CSV format for external analysis
- **Real-time Updates**: Statistics update automatically as tasks are modified

## 🏗️ Project Structure

```
todo-app/
├── manage.py                 # Django management script
├── README.md                # This file
├── todo_project/            # Main Django project
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── todo/                    # Todo application
│   ├── __init__.py
│   ├── admin.py            # Admin interface configuration
│   ├── apps.py
│   ├── forms.py            # Task form definition
│   ├── models.py           # Task model definition
│   ├── urls.py             # App URL patterns
│   ├── views.py            # View functions
│   ├── tests.py
│   └── migrations/         # Database migrations
└── templates/              # HTML templates
    ├── base.html           # Base template
    └── todo/               # Todo app templates
        ├── task_list.html  # Main task list view
        ├── task_form.html  # Create/edit task form
        └── task_confirm_delete.html  # Delete confirmation
```

## 🎨 Design Features

### Modern UI/UX
- **Glass-morphism design** with backdrop blur effects
- **Gradient backgrounds** for visual appeal
- **Responsive layout** that works on all devices
- **Smooth animations** and hover effects
- **Intuitive icons** and visual indicators

### Developer-Friendly
- **Emoji-based priorities** for quick visual recognition
- **Category icons** for easy task organization
- **Overdue detection** with visual warnings
- **Statistics dashboard** for progress tracking
- **Bulk operations** for efficient task management

## 🔧 Customization

### Adding New Categories
Edit `todo/models.py` and add new choices to `CATEGORY_CHOICES`:
```python
CATEGORY_CHOICES = [
    # ... existing choices ...
    ('new_category', 'New Category'),
]
```

### Adding New Priorities
Edit `todo/models.py` and add new choices to `PRIORITY_CHOICES`:
```python
PRIORITY_CHOICES = [
    # ... existing choices ...
    ('new_priority', 'New Priority'),
]
```

### Styling Customization
Modify the CSS in `templates/base.html` to change colors, fonts, or layout.

## 🚀 Deployment

### For Production
1. Set `DEBUG = False` in `settings.py`
2. Configure a production database (PostgreSQL recommended)
3. Set up static file serving
4. Use a production WSGI server (Gunicorn, uWSGI)
5. Configure environment variables for security

### Environment Variables
```bash
export SECRET_KEY='your-secret-key'
export DEBUG=False
export ALLOWED_HOSTS='your-domain.com'
```

## 📝 License

This project is created for educational purposes as part of the Full Stack Software Development program.

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome!

## 📞 Support

For questions or issues, please refer to the Django documentation or create an issue in the repository.

---

**Built with ❤️ for developers who need to track their chaos before it tracks them.** 