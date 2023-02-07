from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Monument


class MonumentListView(ListView):
    template_name = "monuments/monument_list.html"
    model = Monument
    context_object_name = "ctx"

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = Monument.objects.filter(name__iregex=query)
            return object_list
        return Monument.objects.all()


class MonumentDetailView(DetailView):
    template_name = "monuments/monument_detail.html"
    model = Monument
