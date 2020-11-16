from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Publication



def all_publications(request):
    pubs = Publication.objects.all()
    return render(request, "publications/all.html", {"publications": pubs})


class PublicationDetailView(DetailView):
    queryset = Publication.objects.all()
    template_name = "publications/publication.html"


def create_publication(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        text = request.POST.get("text")
        publication = Publication(
            name=name,
            text=text
        )
        publication.save()
        return redirect('publication', pk=publication.pk)

    return render(request, "publications/create.html")