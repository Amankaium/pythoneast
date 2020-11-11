from django.shortcuts import render
from .models import Publication


def all_publications(request):
    pubs = Publication.objects.all()
    return render(request, "publications/all.html", {"publications": pubs})
