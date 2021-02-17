from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Projects
import requests


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


class ProjectListView(ListView):
    template_name = "projects/project-list.html"
    queryset = Projects.objects.all()


class ProjectDetailView(DetailView):
    template_name = "projects/project-detail.html"
    queryset = Projects.objects.all()