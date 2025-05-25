from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'review']
        labels = {
            'title': 'Название фильма',
            'description': 'Описание фильма',
            'review': 'Ваш отзыв',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'review': forms.Textarea(attrs={'rows': 3}),
        }