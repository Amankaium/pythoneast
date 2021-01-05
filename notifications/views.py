from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *


class NotificationsListView(ListView):
    template_name = "notifications/all.html"
    
    def get_queryset(self):
        notifications = InviteNotification.objects.filter(
            user=self.request.user,
            is_readed=False    
        )
        
        return notifications


def accept_invite(request, id):
    notification = InviteNotification.objects.get(id=id)
    notification.is_readed = True
    notification.save()

    invite = notification.invite
    invite.is_accepted = True
    invite.save()

    return redirect('notifications')


def reject_invite(request, id):
    notification = InviteNotification.objects.get(id=id)
    notification.is_readed = True
    notification.save()
    return redirect('notifications')
    
