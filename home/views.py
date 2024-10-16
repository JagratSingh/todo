from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

def home(request):
    tasks = ToDo.objects.all() # Fetch all task from database 
    form = TodoForm() # Create an instance of the form
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid(): # Validate the form
            form.save() # Save the task to the database
        return redirect('/') # Redirect to the homepage
    
    context = {'tasks':tasks, 'form':form}
    
    return render(request, 'index.html', context) # Render the template

def updateTask(request, pk):
    task = ToDo.objects.get(id=pk) # Fetch the task with same id
    form = TodoForm(instance=task) # Populate the form with the existing task
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid(): # Validate the form
            form.save() # Save the updated task
            return redirect('/') # After successfully saving the data it will redirect to home page
    
    context = {'form':form}
    
    return render(request, 'update_task.html', context) # Render the updated template

def deleteTask(request, pk):
    task = ToDo.objects.get(id=pk) # Fetch the task from the database
    
    if request.method == 'POST':
        task.delete() # Delete the task
        return redirect('/') # After deleting the tas, it will redirect to the home page
    
    context = {'task':task}
    
    return render(request, 'delete_task.html', context) # Render the template