from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout


@login_required
def add_workout(request):
    if request.method == 'POST':
        Workout.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            workout_type=request.POST.get('workout_type'),
            difficulty=request.POST.get('difficulty'),
            duration=request.POST.get('duration'),
            notes=request.POST.get('notes'),
        )
        return redirect('/dashboard/')

    return render(request, 'workouts/add_workout.html')


@login_required
def edit_workout(request, id):
    workout = get_object_or_404(Workout, id=id, user=request.user)

    if request.method == 'POST':
        workout.name = request.POST.get('name')
        workout.workout_type = request.POST.get('workout_type')
        workout.difficulty = request.POST.get('difficulty')
        workout.duration = request.POST.get('duration')
        workout.notes = request.POST.get('notes')
        workout.save()
        return redirect('/dashboard/')

    return render(request, 'workouts/edit_workout.html', {
        'workout': workout
    })
