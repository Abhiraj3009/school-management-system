from django.contrib import admin
from .models import Student, Teacher, Classroom, Period

# 1. Define the Inline
class PeriodInline(admin.TabularInline):
    model = Period
    extra = 0  # This prevents showing empty rows by default

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject', 'email')
    search_fields = ('first_name', 'last_name', 'subject')
    list_filter = ('subject',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'first_name', 'last_name', 'classroom')
    search_fields = ('first_name', 'last_name', 'roll_number')
    list_filter = ('classroom', 'date_of_birth')

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name',) # Removed 'teacher' from here!
    inlines = [PeriodInline]

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'period_number', 'subject', 'teacher')
    ordering = ('classroom__name', 'period_number')
    list_filter = ('classroom', 'subject')