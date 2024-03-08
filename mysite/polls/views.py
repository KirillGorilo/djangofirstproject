from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
import datetime
from django.views import generic
from django.template import loader
from django.views.generic import TemplateView, ListView

from .models import Products


class IndexView(generic.ListView):
    template_name = "polls/index.html"
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


def auth(request):
    return render(request, 'polls/register.html')

