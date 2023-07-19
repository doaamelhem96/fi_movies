from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView
from .models import Fiction
from django.urls import reverse_lazy
# Create your views here.

class ListsViews(ListView):
    template_name='fictions/list.html'
    model=Fiction
class DetailsViews(DetailView):
    template_name='fictions/detail.html'
    model=Fiction
class CreatesViews(CreateView):
    template_name='fictions/create.html'
    model=Fiction
    fields= '__all__'
class UpdatesViews(UpdateView):
    template_name='fictions/update.html'
    model=Fiction
    fields= '__all__'
class DeletesViews(DeleteView):
    template_name='fictions/delete.html'
    model=Fiction
    success_url=reverse_lazy("listmovie")