from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView

from todo.models import Todo


class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('login:login')
    redirect_field_name = ''
    template_name = 'todo/index.html'
    context_object_name = 'all_todos'

    def get_queryset(self):
        return Todo.objects.all().filter(user=self.request.user)


class TodoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login:login')
    redirect_field_name = ''
    model = Todo
    fields = ['title', 'description', 'status']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreate, self).form_valid(form)


class TodoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login:login')
    redirect_field_name = ''
    model = Todo
    success_url = reverse_lazy('todo:index')


class TodoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login:login')
    redirect_field_name = ''
    model = Todo
    fields = ['title', 'description', 'status']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return HttpResponseRedirect(reverse('todo:index'))
        else:
            return super(TodoUpdate, self).get(request, *args, **kwargs)


class FilterView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('login:login')
    redirect_field_name = ''
    template_name = 'todo/index.html'
    context_object_name = 'all_todos'

    def get_queryset(self):
        return Todo.objects.all().filter(user=self.request.user, status=self.kwargs['status'])
