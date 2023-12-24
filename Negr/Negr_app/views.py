from django.shortcuts import render, redirect
from .models import Project, Task
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from .forms import ProjectForm, TaskForm, RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse


class TestPage(TemplateView):
    template_name = 'test.html'

    def post(self, request):
        data = request.POST
        return JsonResponse({'resp': data['text']}, safe=False)


class HomeView(ListView):
    model = Project
    paginate_by = 2
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectForm()
        context['projects'] = Project.objects.all()
        return context


# def project(request, **kwargs):
#     project = Project.objects.get(id=kwargs['id'])
#     # tasks = Task.objects.filter(project=project.id)
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             priority = form.cleaned_data['priority']
#             deadline = form.cleaned_data['deadline']
#             status = form.cleaned_data['status']
#             task = Task(name=name, priority=priority, deadline=deadline, project=project, status=status)
#             task.save()
#             return redirect(f'/')
#     else:
#         form = TaskForm()
#         tasks = Task.objects.filter(project=project)
#         return render(request, 'project_page.html', {'project': project, 'tasks': tasks, 'form': form})


class ProjectCreate(TemplateView):
    template_name = 'project_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectForm()
        return context

    def post(self, request):
        data = request.POST
        project = Project(name=data['id_name'])
        project.save()
        print(data)
        return JsonResponse({'resp': data['id_name']}, safe=False)


# class TaskPage(TemplateView):
#     template_name = 'task_page.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         task = Task.objects.get(id=self.kwargs['id'])
#         context['form'] = TaskForm(initial={'name': task.name, 'status': task.status, 'deadline': task.deadline,
#                                             'priority': task.priority})
#         context['task'] = task
#         return context
#
#     def post(self, request, **kwargs):
#         data = request.POST
#         task = Task(name=data['id_name'], status=True if data['id_status'] == 'on' else False,
#                                deadline=data['id_deadline'], priority=data['id_priority'], project_id=self.kwargs['id'])
#         task.save()
#         print(data)
#         resp = render_to_string('task.html', {'task': task})
#         return JsonResponse(resp, safe=False)


class ProjectPage(TemplateView):
    template_name = 'project_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = Project.objects.get(id=self.kwargs['id'])
        task = Task.objects.filter(project=project)
        context['project'] = project
        context['task'] = task
        context['form'] = TaskForm()
        return context

    def post(self, request, **kwargs):
        data = request.POST
        print(data)
        if len(data.keys()) == 5:
            task = Task(name=data['id_name'], status=True if data['id_status'] == 'on' else False, deadline=data['id_deadline'], priority=data['id_priority'], project_id=self.kwargs['id'])
            task.save()
            print(data)
            resp = render_to_string('task.html', {'task': task})
            return JsonResponse(resp, safe=False)

        elif 'id' in data.keys():
            task = Task.objects.get(id=int(data['id']))
            resp = render_to_string('edit_form.html',{'task': task, 'date': task.deadline.strftime('%Y-%m-%d %H:%M')})
            return JsonResponse(resp, safe=False)

        elif 'id_change_name' in data.keys():
            task = Task.objects.get(id=int(data['task']))
            task.name = data['id_change_name']

            task.status = True if data['id_change_status'] == 'on' else False
            task.deadline = data['id_change_deadline']
            task.priority = data['id_change_priority']
            task.save()

            resp = render_to_string('task.html', {'task': task})
            return JsonResponse(resp, safe=False)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        return render(request, 'registration.html', context={'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'registration.html', context={'form': form})


def login1(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username,  password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})

