import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import HistoricalObject, Mail
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HistoricalObjectSerializer
from .forms import EmailForm, HistoricalObjectForm


class HistoricalObjectListView(ListView):
    template_name = "object_list.html"
    context_object_name = "ctx"

    def get_queryset(self):
        object_type = self.kwargs['object_type']
        # query = self.request.GET.get('search')
        # if query:
        #     query_set = HistoricalObject.objects.filter(object_type=query)
        #     return query_setg
        # query_set = HistoricalObject.objects.all()
        query_set = HistoricalObject.objects.filter(object_type__name__iregex=object_type)
        return query_set


class HistoricalObjectDetailView(DetailView):
    template_name = "object_detail.html"
    context_object_name = "ctx"
    model = HistoricalObject


def add_historical_object(request):
    ctx = {'form': HistoricalObjectForm}
    return render(request, 'object_create.html', ctx)


class HistoricalObjectCreateView(CreateView):
    model = HistoricalObject
    fields = "__all__"
    template_name = "object_create.html"
    context_object_name = "ctx"
    success_url = reverse_lazy("home")


class EmailCreateView(CreateView):
    model = Mail
    fields = ['mail']
    # form_class = EmailForm
    success_url = reverse_lazy("home")


def existing_email(request):
    if request.method == 'GET':
        email = request.GET.get('email', '')
        print(email)
        try:
            Mail.objects.get(mail=email)
            return HttpResponse(json.dumps({"email": False}))
        except Exception as ex:
            print(ex)
            return HttpResponse(json.dumps({"email": True}))

# class HistoricalObjectAPIView(generics.ListAPIView):
#     queryset = HistoricalObject.objects.all()
#     serializer_class = HistoricalObjectSerializer


class HistoricalObjectAPIList(generics.ListCreateAPIView):
    queryset = HistoricalObject.objects.all()
    serializer_class = HistoricalObjectSerializer


class HistoricalObjectAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            objects = HistoricalObject.objects.all()
            return Response({'posts': HistoricalObjectSerializer(objects, many=True).data})

        try:
            ob = HistoricalObject.objects.get(pk=pk)
            return Response({"post": HistoricalObjectSerializer(ob).data})
        except:
            return Response({"error": "Object does not exist"})

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

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method DELETE is not allowed"})

        try:
            HistoricalObject.objects.get(pk=pk).delete()
        except:
            return Response({"error": "Object does not exist"})

        return Response({"post": f"deleted post {pk}"})
