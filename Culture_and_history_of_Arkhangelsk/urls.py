from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.CommonSearchListView.as_view(), name='home'),
    path('historical_object/', include('historical_objects.urls')),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('exit/', auth_views.LogoutView.as_view(next_page='home'), name='exit'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('user_profiles/', include('user_profiles.urls')),
]

# нужно что-бы показывались картинки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
