from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.user_register,name='register'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('settings/',views.user_settings , name='user-settings')
]
