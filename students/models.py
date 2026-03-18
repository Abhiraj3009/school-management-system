from django.db import models

class Teacher(models.Model):
    # 1. Define the choices as a list of tuples (Value, Label)
    SUBJECT_CHOICES = [
        ('Maths', 'Maths'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('SST', 'Social Studies'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # 2. Add 'choices' to the field
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Prof. {self.last_name} ({self.get_subject_display()})"

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
    # 3. Use the same choices here!
    subject = models.CharField(max_length=20, choices=Teacher.SUBJECT_CHOICES)
    period_number = models.PositiveIntegerField()

    class Meta:
        unique_together = ('classroom', 'period_number')

    def __str__(self):
        return f"{self.classroom.name} - P{self.period_number} ({self.subject})"
    
    def clean(self):
        # Check if the teacher is already busy in another classroom during the same period
        if Period.objects.filter(teacher=self.teacher, period_number=self.period_number).exclude(pk=self.pk).exists():
            raise ValidationError(f"{self.teacher} is already assigned to another class in Period {self.period_number}!")

    def save(self, *args, **kwargs):
        self.full_clean() # This ensures the 'clean' method above is called
        super().save(*args, **kwargs)