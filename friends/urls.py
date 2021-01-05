from django.urls import path
from .views import *

urlpatterns = [
    path("invite/<int:id>/", add_invite, name="invite"),
    path("friends/", FriendsListView.as_view(), name="friends"),
    path("delete/", delete_friend, name="delete-friend"),
]