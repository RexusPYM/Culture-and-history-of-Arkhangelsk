from django.urls import path
from . import views


app_name = "monuments"


urlpatterns = [
    path('list_monument/', views.MonumentListView.as_view(), name='list_monument'),
    path('detail_monument/<int:pk>', views.MonumentDetailView.as_view(), name='detail_monument'),

]
