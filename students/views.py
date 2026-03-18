from django.shortcuts import render, get_object_or_404
from .models import Classroom

def classroom_list(request):
    # Grab all classes from the database
    classrooms = Classroom.objects.all().order_by('name')
    return render(request, 'students/classroom_list.html', {'classrooms': classrooms})

def classroom_detail(request, pk):
    # Grab one specific class or show a 404 error if it doesn't exist
    classroom = get_object_or_404(Classroom, pk=pk)
    # Get all periods for THIS class, ordered by period number
    periods = classroom.periods.all().order_by('period_number')
    return render(request, 'students/classroom_detail.html', {
        'classroom': classroom,
        'periods': periods
    })