from django.shortcuts import render, get_object_or_404

# Create your views here.


# importing models

from students.models import Profile


def index(request):
    students_list = Profile.objects.order_by('id')
    context = {
        'students_list': students_list
    }
    return render(request, 'students/index.html', context)


def single(request, student_id):
    profile = get_object_or_404(Profile, pk=student_id)
    return render(request, 'students/profile.html', {'profile': profile})


def result(request, student_id):
    return "Something"