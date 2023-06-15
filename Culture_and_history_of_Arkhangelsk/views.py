from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from historical_objects.models import HistoricalObject


class CommonSearchListView(ListView):
    template_name = "object_list.html"
    context_object_name = "ctx"

    def get_queryset(self):
        # letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        # alph_dic = {i: letters.index(i) for i in letters}

        # query = self.request.GET.get('search')
        # if query:
        #     query_sets = [Monument.objects.filter(name__iregex=query),
        #                   Culture.objects.filter(name__iregex=query),
        #                   Showplace.objects.filter(name__iregex=query), ]
        #     query_list = []
        #     for query_set in query_sets:
        #         for query in query_set:
        #             query_list.append(query)
        #     return query_list
        #
        # query_sets = [Monument.objects.all(),
        #               Culture.objects.all(),
        #               Showplace.objects.all(), ]
        # query_list = []
        # for query_set in query_sets:
        #     for query in query_set:
        #         query_list.append(query)
        # return query_list
        # return query_list.sort(key=alph_dic.get)

        query = self.request.GET.get('search')
        if query:
            query_set = HistoricalObject.objects.filter(name__iregex=query)
            return query_set
        query_set = HistoricalObject.objects.all()
        return query_set


