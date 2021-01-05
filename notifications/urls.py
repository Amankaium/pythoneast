from django.urls import path
from .views import *

urlpatterns = [
    path("", NotificationsListView.as_view(), name="notifications"),
    path("accept-invite/<int:id>/", accept_invite, name="accept-invite"),
    path("reject-invite/<int:id>/", reject_invite, name="reject-invite"),

]