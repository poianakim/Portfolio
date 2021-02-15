from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Projects


class ProjectListView(ListView):
    template_name = "projects/project-list.html"
    queryset = Projects.objects.all()


class ProjectDetailView(DetailView):
    template_name = "projects/project-detail.html"
    queryset = Projects.objects.all()