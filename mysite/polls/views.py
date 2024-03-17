from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


def index(request):
    return render(request, 'polls/products.html')

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