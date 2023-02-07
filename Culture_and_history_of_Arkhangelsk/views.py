from django.shortcuts import render
from django.views.generic import ListView

from monuments.models import Monument
from culture.models import Culture
from showplaces.models import Showplace


class CommonSearchListView(ListView):
    template_name = "object_list.html"
    context_object_name = "ctx"

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            query_sets = [Monument.objects.filter(name__iregex=query),
                          Culture.objects.filter(name__iregex=query),
                          Showplace.objects.filter(name__iregex=query), ]
            query_list = []
            for query_set in query_sets:
                for query in query_set:
                    query_list.append(query)
                    # query['object_type'] = str(type(query).__name__)
            return query_list
        return
