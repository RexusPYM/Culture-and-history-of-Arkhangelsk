from django.urls import path
from . import views

app_name = "culture"


urlpatterns = [
    path('list_culture/', views.CustomListView.as_view(), name='list_culture'),
    path('detail_culture/<int:pk>', views.CustomDetailView.as_view(), name='detail_culture')
]
