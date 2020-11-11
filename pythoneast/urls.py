from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('publication/', include("publications.urls")),
    path("", include("core.urls")),

]
