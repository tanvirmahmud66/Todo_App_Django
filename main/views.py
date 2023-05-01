from django.shortcuts import render, redirect
from .models import TodoModel
# Create your views here.


def index(request):
    todos = TodoModel.objects.all()
    if request.method == "POST":
        todo = request.POST['todo']
        new_todo = TodoModel.objects.create(
            todo=todo
        )
        new_todo.save()
        return redirect('index')
    return render(request, 'index.html', {
        "todos": todos,
    })


def is_complete(request, id):
    todo = TodoModel.objects.get(id=id)
    if todo.is_complete:
        todo.is_complete = False
        todo.save()
        return redirect('index')
    else:
        todo.is_complete = True
        todo.save()
        return redirect('index')


def todo_delete(request, id):
    todo = TodoModel.objects.get(id=id)
    todo.delete()
    return redirect('index')


def edit_todo(request, id):
    todo = TodoModel.objects.get(id=id)
    if request.method == "POST":
        edited_todo = request.POST['todo']
        todo.todo = edited_todo
        todo.save()
        return redirect('index')
    return render(request, 'edit.html', {
        "todo": todo
    })
