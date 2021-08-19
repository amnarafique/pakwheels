from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from users.views import register, my_account, update_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),
    path('update_profile/', update_profile, name='update_profile'),


]
