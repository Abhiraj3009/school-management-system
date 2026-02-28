from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # This displays these columns in the list view
    list_display = ('roll_number', 'first_name', 'last_name', 'email')
    
    # This adds a search bar
    search_fields = ('first_name', 'last_name', 'roll_number')