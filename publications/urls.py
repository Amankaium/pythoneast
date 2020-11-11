from django.urls import path
from .views import all_publications

urlpatterns = [
    path("all/", all_publications, name='all-publications'),
]