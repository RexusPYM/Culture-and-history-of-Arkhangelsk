from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Showplace


class ShowplaceListView(ListView):
    template_name = "showplaces/showplace_list.html"
    model = Showplace
    context_object_name = "ctx"

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = Showplace.objects.filter(name__iregex=query)
            return object_list
        return Showplace.objects.all()


class ShowplaceDetailView(DetailView):
    template_name = "showplaces/showplace_detail.html"
    model = Showplace
    context_object_name = "ctx"
