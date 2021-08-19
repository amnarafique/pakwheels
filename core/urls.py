
from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include

from core import settings
from home.views import upload_car

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('home.urls')),
    path('upload_car/', upload_car, name='upload_car'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


