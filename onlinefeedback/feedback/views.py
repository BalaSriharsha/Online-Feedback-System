from django.shortcuts import render, redirect

from .models import Lecturer
from .forms import FeedbackForm

# Create your views here.


def home(request):
    lecturers_list = Lecturer.objects.filter(
        section='A').filter(department='ECE').filter(year='3rd')
    args = {'lecturers_list': lecturers_list}
    return render(request, 'feedback/home.html', args)


def feedback(request, id):
    lecturer_id = Lecturer.objects.get(id=1)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.lecturer = lecturer_id
            feedback.save()
            return redirect('/')
    else:
        form = FeedbackForm()

        args = {'form': form, 'lecturer': lecturer_id.id}
        return render(request, 'feedback/feedback.html', args)
