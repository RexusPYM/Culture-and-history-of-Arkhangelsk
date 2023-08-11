from django.urls import path
from . import views


app_name = "historical_object"


urlpatterns = [
    path('list_object/<str:object_type>', views.HistoricalObjectListView.as_view(), name='list_object'),
    path('detail_object/<int:pk>', views.HistoricalObjectDetailView.as_view(), name='detail_object'),
    path('create_object/', views.add_historical_object),
    path('list_object_api', views.HistoricalObjectAPIList.as_view()),
    path('list_object_api/<int:pk>', views.HistoricalObjectAPIList.as_view()),
    path('subscribe_email', views.EmailCreateView.as_view(), name='subsribe_email'),
    path('existing_email', views.existing_email, name='existing_email'),
]
