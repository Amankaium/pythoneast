from django.forms import ModelForm, CharField
from .models import Publication


class PublicationForm(ModelForm):
    name = CharField(max_length=10, help_text='Напишите название публикации')

    class Meta:
        model = Publication
        fields = ["name", "text", "image"]