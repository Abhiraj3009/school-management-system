import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User
from students.models import Student, Teacher

def create_credentials():
    # Helper function to process users
    def process_people(queryset, role_name):
        print(f"--- Creating {role_name} accounts ---")
        for person in queryset:
            # Username: Jessa_Propper
            username = f"{person.first_name}_{person.last_name}"
            # Password: jessapropper (all lowercase, no underscore)
            password = f"{person.first_name.lower()}{person.last_name.lower()}"
            
            if not User.objects.filter(username=username).exists():
                # Create the Django User
                user = User.objects.create_user(username=username, password=password)
                person.user = user
                person.save()
                print(f"Created: {username} | Password: {password}")
            else:
                print(f"Skipped: {username} (Already exists)")

    process_people(Teacher.objects.all(), "Teacher")
    process_people(Student.objects.all(), "Student")

if __name__ == "__main__":
    create_credentials()