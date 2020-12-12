from django import forms
from .models import Publication


class PublicationForm(forms.ModelForm):
    # name = CharField(max_length=10, help_text='Напишите название публикации')
    # test = forms.CharField(required=True)
    class Meta:
        model = Publication
        fields = ["name", "text", "image"]