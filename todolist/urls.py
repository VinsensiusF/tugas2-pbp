from django.urls import path
from todolist.views import add_task, register, show_task , login_user, logout_user, todolist_ajax, show_json, todolist_ajax_submit
app_name = 'todolist'

urlpatterns = [
    path("show-json", show_json, name='show-json'),
    path('', show_task, name='todolist'), 
    path('json/', todolist_ajax, name="todolist-ajax"),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'), 
    path('create-task/', add_task, name = 'create-task'),
    path('add', todolist_ajax_submit, name="submit-ajax")
]