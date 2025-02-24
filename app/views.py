from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
from rest_framework import viewsets, generics
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import datetime
from django.http import HttpResponse, HttpResponseNotAllowed
from django.urls import reverse



# Create your views here.
def index(request):
    return render(request, "app/index.html")

def new_task(request):
    if request.method != "POST":
        form = TaskForm()
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    data = {"form": form}
    return render(request, "app/new-task.html", data)
        
        


def task_list(request):
    tasks_list = Task.objects.all()
    data = {"tasks_list": tasks_list}
    return render(request, "app/task-list.html", data)

def change_task_status(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        # Obtener el valor del select
        completed = request.POST.get('completed') == 'True'
        task.complete = completed
        task.save()
        # Generar el HTML del select actualizado
        select_html = '''
        <select name="completed" hx-post="{url}" hx-swap="outerHTML" hx-target="this">
            <option value="True" {yes_selected}>Yes</option>
            <option value="False" {no_selected}>No</option>
        </select>
        '''.format(
            url=reverse('change_task_status', args=[task.id]),
            yes_selected='selected' if task.complete else '',
            no_selected='selected' if not task.complete else ''
        )
        return HttpResponse(select_html)
    else:
        return HttpResponseNotAllowed(['POST'])

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    
    return render(request, "app/edit-task.html", {"form": form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("task_list")
    
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

def login_view(request):
    return render(request, "app/login.html")

def logout_view(request):
    if request.method == "POST":
        # Eliminar la cookie de autenticación
        return redirect("login")
    return redirect ("index")

def task_duedate_reminder(request):
    today = datetime.date.today()
    tasks = Task.objects.filter(due_date__lt=today)
    data = {"tasks": tasks}
    return render(request, "app/task-duedate-reminder.html", data)


