from django.shortcuts import render
from .models import Task
from django.shortcuts import get_object_or_404, redirect
from .forms import UserRegisterForm, LoginForm, CreateTaskForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'todoApp/index.html')



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            return redirect('my-login')
    
    else:
        form = UserRegisterForm()

    context = {'form':form}
    return render(request, 'todoApp/register.html', context=context)

def my_login(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    
    else:
        form = LoginForm()
    
    context = {'form':form}
    return render(request, 'todoApp/my_login.html', context=context)

@login_required(login_url='my-login')
def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            user_task = form.save(commit=False)
            user_task.user = request.user
            user_task.save()
            
            return redirect('dashboard')
    
    else:
        form = CreateTaskForm()
        
    context = {'form':form}
    return render(request, 'todoApp/create_task.html', context=context)

@login_required(login_url='my-login')
def dashboard(request):
    user_task = Task.objects.filter(user=request.user)
    context = {'user_task':user_task}
    return render(request, 'todoApp/dashboard.html', context=context)

@login_required(login_url='my-login')
def task(request, pk):
    task = get_object_or_404(Task, id=pk)
    context = {'task':task}
    return render(request, 'todoApp/task_view.html', context=context)

@login_required(login_url='my-login')
def my_logout(request):
        logout(request)
        return redirect('my-login')
        
