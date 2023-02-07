from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Culture


class CustomListView(ListView):
    template_name = "culture/culture_list.html"
    model = Culture
    context_object_name = "ctx"

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = Culture.objects.filter(name__iregex=query)
            return object_list
        return Culture.objects.all()


class CustomDetailView(DetailView):
    template_name = "culture/culture_detail.html"
    model = Culture
    context_object_name = "ctx"
