from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-name', 'placeholder': 'name'}), label='')
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-comment', 'placeholder': 'comment'}), label='')

    class Meta:
        model = Comment
        fields = ('name', 'comment',)