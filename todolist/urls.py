from django.urls import path
from todolist.views import add_task, register, show_task 
from todolist.views import login_user 
from todolist.views import logout_user 

app_name = 'todolist'

urlpatterns = [
    path('', show_task, name='todolist'), 
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'), 
    path('create-task/', add_task, name = 'create-task'),
]