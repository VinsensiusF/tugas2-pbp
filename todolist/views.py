from re import T
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from todolist.forms import TaskForm
from todolist.models import Task
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.core import serializers

# Create your views here.
def get_success_url():
    return reverse('')

def show_json(request):
    data = Task.objects.all()
    task_item = data.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", task_item), content_type="application/json")

@login_required(login_url='/todolist/login/')
def show_task(request):
    task_item = Task.objects.all()
    task_item = task_item.filter(user=request.user)
    context = {
        'list_task': task_item,
        'nama': 'Vinsensius Ferdinando',
        'npm': '2106751221',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist_ajax.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(request.POST)
        # check whether it's valid:
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect('/todolist')
    else:
        form = TaskForm()

    return render(request, 'form.html', {'form': form})

@login_required(login_url='/todolist/login/')
def todolist_ajax(request):
    context = {
        'nama': 'Vinsensius Ferdinando',
        'npm': '2106751221',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist_ajax.html", context)

@login_required(login_url='/todolist/login/')
def todolist_ajax_submit(request):
    if (request.method == "POST"):
        form = TaskForm(request.POST or None)
        if (form.is_valid()):
            user = request.user
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            new_todolist_item = Task.objects.create(user=user, title=title, description=description)
            return JsonResponse({'title':title,
                                'description':description
                                })
