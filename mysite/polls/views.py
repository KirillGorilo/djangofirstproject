from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,    
    DeleteView,
)
from .models import ToDoList, ToDoItem


class ListListView(ListView):
    model = ToDoList
    template_name = "polls/index.html"


class ItemListView(ListView):
    model = ToDoItem
    template_name = "polls/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Создать список"
        return context

class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date", 
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Создать новую задачу"
        return context

    def get_success_url(self):
        return reverse("polls:list", args=[self.object.todo_list_id])


class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Изменить задачу"
        return context

    def get_success_url(self):
        return reverse("polls:list", args=[self.object.todo_list_id])


class ListDelete(DeleteView):
    model = ToDoList
    # You have to use reverse_la    zy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("polls:home")


class ItemDelete(DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context


def register(request):      
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'polls/login.html')
    else:
        form = RegisterUserForm()
    return render(request, 'polls/registerF.html', {'form': form})

def logout_user(request):
    logout(request)
    return render(request, 'polls/logout.html')
    # return HttpResponseRedirect(reverse('polls:home'))

def account(request):
    return render(request, 'polls/account.html')


class CustomLoginView(auth_views.LoginView):
    def get_success_url(self):
        return reverse_lazy('polls:home')