from django.contrib import admin
from .models import *


# admin.site.register(Invite)
@admin.register(Invite)
class InviteAdmin(admin.ModelAdmin):
    exclude = ["name"]