import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import HistoricalObject, Mail, TemporaryHistoricalObject, ProposedHistoricalObject
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HistoricalObjectSerializer
from .forms import EmailForm, HistoricalObjectForm, ProposeHistoricalObjectForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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


# def add_historical_object(request):
#     ctx = {'form': HistoricalObjectForm}
#     return render(request, 'object_create.html', ctx)


class ProposeHistoricalObjectCreateView(LoginRequiredMixin, CreateView):
    form_class = ProposeHistoricalObjectForm
    template_name = "object_create.html"
    context_object_name = "ctx"
    success_url = reverse_lazy("home")
    raise_exception = True

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return super().form_valid(form)


class CheckHistoricalObjectsListView(ListView):
    template_name = "object_checking.html"
    context_object_name = "ctx"

    def get_queryset(self):
        query_set = ProposedHistoricalObject.objects.all()
        return query_set


class EmailCreateView(CreateView):
    model = Mail
    fields = ['mail']
    # form_class = EmailForm
    success_url = reverse_lazy("home")


def existing_email(request):
    if request.method == 'GET':
        print('passing request')
        email = request.GET.get('email', '')
        print(email)
        try:
            Mail.objects.get(mail=email)
            return HttpResponse(json.dumps({"email": False}))
        except Exception as ex:
            print(ex)
            return HttpResponse(json.dumps({"email": True}))


def add_historical_object_to_main_table(request, **kwargs):
    proposed_historical_object_id = kwargs['pk']
    proposed_historical_object = ProposedHistoricalObject.objects.get(pk=proposed_historical_object_id)

    new_historical_object = HistoricalObject()
    new_historical_object.name = proposed_historical_object.name
    new_historical_object.object_type = proposed_historical_object.object_type
    new_historical_object.description = proposed_historical_object.description
    new_historical_object.picture = proposed_historical_object.picture
    new_historical_object.author = proposed_historical_object.author
    new_historical_object.checked_by = request.user
    new_historical_object.save()

    proposed_historical_object.delete()

    return redirect("historical_object:check_object")


def delete_historical_object_from_proposed_table(request, **kwargs):
    proposed_historical_object_id = kwargs['pk']
    proposed_historical_object = ProposedHistoricalObject.objects.get(pk=proposed_historical_object_id)
    proposed_historical_object.delete()

    return redirect("historical_object:check_object")


def save_db(request):
    print('kek')
    # Получаем объекты (записи) из исходной модели
    data = TemporaryHistoricalObject.objects.all()

    # Копируем данные из исходной модели в целевую модель
    for object_data in data:
        new_entry = HistoricalObject()
        new_entry.name = object_data.name  # Замени поле1 и поля согласно своей модели
        new_entry.object_type = object_data.object_type
        new_entry.description = object_data.description
        new_entry.picture = object_data.picture

        new_entry.save()  # Сохраняем скопированные данные в новой модели

    return HttpResponse('Данные скопированы')

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
