from django.urls import path
from . import views

app_name = "user_profiles"


urlpatterns = [
    path('make_comment/<int:historical_object_id>', views.MakeComment.as_view(), name='make_comment')
]
