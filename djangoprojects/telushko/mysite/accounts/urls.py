
from django.urls import path
from . import views

from django.contrib import admin


urlpatterns = [
     path('admin/', admin.site.urls),
    path('register/',views.register,name="register"),
    path('login/',views.login,name='login'),
    

   
]
