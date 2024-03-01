from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
import datetime
from django.views import generic

from .models import Products


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_product_list"

    def get_queryset(self):
        return Products.objects.all()


class DetailView(generic.DetailView):
    model = Products
    
