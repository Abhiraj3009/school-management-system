from django.contrib import admin
from .models import Student, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # This displays these columns in the list view
    list_display = ('roll_number', 'first_name', 'last_name', 'email')
    
    # This adds a search bar
    search_fields = ('first_name', 'last_name', 'roll_number')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # Displays these columns for Teachers
    list_display = ('first_name', 'last_name', 'subject', 'email')
    
    # Allows you to search by name or their specialty subject
    search_fields = ('first_name', 'last_name', 'subject')