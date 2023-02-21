from django.shortcuts import render,HttpResponse
from .models import Todos
# Create your views here.
def index(request):
   
    tasks=Todos.objects.all()
    return render(request,'todos/index.html',{'tasks':tasks})