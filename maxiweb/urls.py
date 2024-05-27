
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('webapp1/', include("webapp1.urls")),

]
