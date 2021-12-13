from django.shortcuts import render, redirect
from .models import todolist
from .forms import Todolist_appForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todo_items = todolist.objects.order_by('id')
    form = Todolist_appForm()
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todolist_app/index.html', context)

@require_POST
def addTodoItem(request):
    form = Todolist_appForm(request.POST)
    if form.is_valid():
        new_todo = todolist(text= request.POST['text'])
        new_todo.save()
    return redirect(index)

def completedTodo(request, todo_id):
    todo = todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    todolist.objects.filter(completed__exact= True).delete()
    return redirect('index')

def deleteAll(request):
    todolist.objects.all().delete()
    return redirect('index')