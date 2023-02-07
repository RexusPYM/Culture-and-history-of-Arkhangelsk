from django.urls import path
from . import views

app_name = "showplaces"


urlpatterns = [
    path('list_showplace/', views.ShowplaceListView.as_view(), name='list_showplace'),
    path('detail_showplace/<int:pk>', views.ShowplaceDetailView.as_view(), name='detail_showplace')
]
