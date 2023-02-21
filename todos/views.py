from django.shortcuts import render,redirect
from .models import Todos
from .forms import todoForm
# Create your views here.
def index(request):
    if request.method=='POST':
        form=todoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        tasks=Todos.objects.all()
        return render(request,'todos/index.html',{'tasks':tasks})
    
def delet(request,id):
    task=Todos.objects.get(pk=id)
    task.delete()
    return redirect('index')

def delet_all(request):
    task=Todos.objects.all()
    task.delete()
    return redirect('index')
        