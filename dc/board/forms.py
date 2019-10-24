from django import forms
from .models import Poster


class PosterForm(forms.ModelForm):
        # created_at = forms.DateField(
        #     widget=forms.DateInput(attrs={'type': 'date'}))
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Poster
        fields = ('title', 'content',)
