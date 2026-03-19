from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Classroom

@login_required
def classroom_list(request):
    # Now only logged-in users can see the list
    classrooms = Classroom.objects.all().order_by('name')
    return render(request, 'students/classroom_list.html', {'classrooms': classrooms})

@login_required
def classroom_detail(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    periods = classroom.periods.all().order_by('period_number')
    students = classroom.students.all().order_by('last_name')

    return render(request, 'students/classroom_detail.html', {
        'classroom': classroom,
        'periods': periods,
        'students': students
    })

@login_required
def login_success(request):
    """
    The 'Traffic Controller' that sends Admins to the back-end 
    and Students/Teachers to the front-end.
    """
    if request.user.is_superuser:
        return redirect('admin:index')
    else:
        return redirect('classroom_list')