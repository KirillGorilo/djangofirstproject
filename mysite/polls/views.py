from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.views.generic import TemplateView, ListView
from .models import Products
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    template_name = "polls/products.html"
    context_object_name = "latest_product_list"

    def get_queryset(self):
        return Products.objects.all()


class DetailView(generic.DetailView):
    model = Products


def outputData(request):
    template = loader.get_template("polls/test.html")
    context = {
        "last_name": "kir",
        "django": "the web framework for perfectionists with deadlines"
    }
    return HttpResponse(template.render(context, request))


class PublisherListView(ListView):
    model = Products


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


# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)

#     return render(request, 'polls/register_done.html')

def logout_user(request):
    logout(request)
    return render(request, 'polls/logout.html')
    # return HttpResponseRedirect(reverse('polls:home'))

def account(request):
    return render(request, 'polls/account.html')


class CustomLoginView(auth_views.LoginView):
    def get_success_url(self):
        return reverse_lazy('polls:home')