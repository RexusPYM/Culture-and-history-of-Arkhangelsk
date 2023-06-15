from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import HistoricalObject
from django.urls import reverse_lazy
from monuments.models import Monument
from culture.models import Culture
from showplaces.models import Showplace
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HistoricalObjectSerializer


class HistoricalObjectListView(ListView):
    template_name = "object_list.html"
    context_object_name = "ctx"

    def get_queryset(self):
        object_type = self.kwargs['object_type']
        # query = self.request.GET.get('search')
        # if query:
        #     query_set = HistoricalObject.objects.filter(object_type=query)
        #     return query_set
        # query_set = HistoricalObject.objects.all()
        query_set = HistoricalObject.objects.filter(object_type__name__iregex=object_type)
        return query_set


class HistoricalObjectDetailView(DetailView):
    template_name = "object_detail.html"
    context_object_name = "ctx"
    model = HistoricalObject


class HistoricalObjectCreateView(CreateView):
    model = HistoricalObject
    fields = "__all__"
    template_name = "object_create.html"
    context_object_name = "ctx"
    success_url = reverse_lazy("home")


# class HistoricalObjectAPIView(generics.ListAPIView):
#     queryset = HistoricalObject.objects.all()
#     serializer_class = HistoricalObjectSerializer


class HistoricalObjectAPIView(APIView):
    def get(self, request):
        o = HistoricalObject.objects.all()
        return Response({'posts': HistoricalObjectSerializer(o, many=True).data})

    def post(self, request):
        serializer = HistoricalObjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # post_new = HistoricalObject.objects.create(
        #     name=request.data['name'],
        #     object_type=request.data['object_type'],
        #     description=request.data['description'],
        #     picture=request.data['picture'],
        # )

        return Response({'posts': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT is not allowed"})

        try:
            instance = HistoricalObject.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = HistoricalObjectSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"posts": serializer.data})
