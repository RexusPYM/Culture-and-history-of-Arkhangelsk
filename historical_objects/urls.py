from django.urls import path
from . import views


app_name = "historical_object"


urlpatterns = [
    path('list_object/<str:object_type>', views.HistoricalObjectListView.as_view(), name='list_object'),
    path('detail_object/<int:pk>', views.HistoricalObjectDetailView.as_view(), name='detail_object'),
    # path('create_object/', views.HistoricalObjectCreateView.as_view(), name='create_object'),
    path('api_hist_ob', views.HistoricalObjectAPIView.as_view()),
    path('list_object_api', views.HistoricalObjectAPIList.as_view()),
    path('list_object_api/<int:pk>', views.HistoricalObjectAPIList.as_view()),
    path('subscribe_email', views.EmailCreateView.as_view(), name='subsribe_email'),
    path('existing_email', views.existing_email, name='existing_email'),
    path('propose_object/', views.ProposeHistoricalObjectCreateView.as_view(), name='propose_object'),
    path('list_checking_object/', views.CheckHistoricalObjectsListView.as_view(), name='check_object'),
    path('add_historical_object_to_main_table/<int:pk>', views.add_historical_object_to_main_table, name='add_object'),
    path('delete_historical_object_from_proposed_table/<int:pk>', views.delete_historical_object_from_proposed_table,
         name='delete_object'),
    # path('save_db', views.save_db, name='save_db')
]
