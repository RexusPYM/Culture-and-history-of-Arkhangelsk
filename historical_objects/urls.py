from django.urls import path
from . import views


app_name = "historical_object"


urlpatterns = [
    path('list_object/<str:object_type>', views.HistoricalObjectListView.as_view(), name='list_object'),
    path('detail_object/<int:pk>', views.HistoricalObjectDetailView.as_view(), name='detail_object'),
    path('create_object/', views.HistoricalObjectCreateView.as_view()),
    path('list_object_api', views.HistoricalObjectAPIView.as_view()),
    path('list_object_api/<int:pk>', views.HistoricalObjectAPIView.as_view()),
]
