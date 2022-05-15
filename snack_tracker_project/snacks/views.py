from django.shortcuts import render
from django.views.generic import  ListView, TemplateView,DetailView
from .models import Snack


# Create our views here.
class HomeView(TemplateView):
    template_name="base.html"

class SnackListView(ListView):
    template_name="snack_list.html"

    model=Snack


class SnackDetailView(DetailView):
    template_name="snack_detail.html"
    model=Snack