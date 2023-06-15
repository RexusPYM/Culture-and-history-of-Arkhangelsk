from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.CommonSearchListView.as_view(), name='home'),
    path('historical_object/', include('historical_objects.urls')),
]

# нужно что-бы показывались картинки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
