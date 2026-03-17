from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Prof. {self.last_name} ({self.subject})"

class Classroom(models.Model):
    name = models.CharField(max_length=50)  # e.g., "STD 1"
    
    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField(auto_now_add=True)
    # Move this inside the class properly
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, blank=True, related_name="students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# NEW: This represents one cell in your timetable image
class Period(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="periods")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50) 
    period_number = models.PositiveIntegerField() # 1, 2, 3, 4, or 5

    class Meta:
        # This makes sure you don't accidentally put two subjects in the same slot for one class
        unique_together = ('classroom', 'period_number')

    def __str__(self):
        return f"{self.classroom.name} - P{self.period_number} ({self.subject})"