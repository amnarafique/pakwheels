from django.conf.urls.static import static
from django.urls import path

from core import settings
from users.views import my_account
from .views import home_page, cars_list, read_more, delete_car, update_car, search, owner_cars

urlpatterns = [
    path('', home_page, name='home_page'),
    path('my_account/', my_account, name='my_account'),
    path('cars_list/', cars_list, name='cars_list'),
    path('read_more/<int:pk>/', read_more, name='read_more'),
    path('delete_car/<int:pk>/', delete_car, name='delete_car'),
    path('update_car/<int:pk>/', update_car, name='update_car'),
    path('search/', search, name='search'),
    path('owner_cars/', owner_cars, name='owner_cars'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


