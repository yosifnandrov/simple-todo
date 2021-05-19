from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET

from my_todo.forms import TodoForm
from my_todo.models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos,
    }
    return render(request,'index.html',context)

def create(request):
    if request.method == "GET":
        form = TodoForm()
        context = {
            'form':form,
        }
        return render(request,'create.html',context)
    form = TodoForm(request.POST)
    if form.is_valid():
        form.save()
        todos = Todo.objects.all()
        context = {
            'todos': todos
        }
        return render(request,'index.html',context)
    return render(request, 'create.html',{'form':form})


def delete(request,pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "GET":
        todo.delete()
    return redirect('index')

def edit(request,pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "GET":
        form = TodoForm(instance=todo)
        context = {
            'todo':todo,
            'form':form,
        }
        return render(request,'edit.html',context)
    form = TodoForm(request.POST,instance=todo)
    if form.is_valid():
        todo.save()
        return redirect('index')
    return render(request,'edit.html',{'form':form})

def check(request, pk):
    if request.method == "GET":
        todo = Todo.objects.get(pk=pk)
        todo.check = not todo.check
        todo.save()
        return redirect('index')