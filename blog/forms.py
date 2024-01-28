from .models import Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','concept','document','status')
    concept = forms.CharField(widget=SummernoteWidget)
    document = forms.CharField(widget=SummernoteWidget)
