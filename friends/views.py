from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Invite

def add_invite(request, id):
    user_1 = request.user
    user_2 = User.objects.get(id=id)
    invite = Invite(user_1=user_1, user_2=user_2)
    invite.save()
    return redirect('users')


class FriendsListView(ListView):
    template_name = 'friends/friends.html'
    
    def get_queryset(self):
        users = User.objects.filter( # TODO
            is_active=True,
            friend_2__user_1=self.request.user,
            friend_2__is_accepted=True
        )
        return users


def delete_friend(request):
    form = request.POST
    user_id = int(form.get("user"))
    friend = User.objects.get(id=user_id)
    source = request.user
    invites = Invite.objects.filter( # TODO
        user_1=source,
        user_2=friend
    )
    invites.delete()
    return redirect('friends')