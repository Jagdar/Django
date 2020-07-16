


from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
   # path('register/',views.register,name="register"),
    path('accounts/',include('accounts.urls'))
  
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
