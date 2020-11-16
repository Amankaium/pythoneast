from django.urls import path
from .views import *

urlpatterns = [
    path("all/", all_publications, name='all-publications'),
    path("<int:pk>", PublicationDetailView.as_view(), name='publication'),
    path("create/", create_publication, name='create-publication'),
]