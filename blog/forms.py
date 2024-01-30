from .models import Post
from django import forms
from django_summernote.widgets import SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','concept','document','status')
    concept = forms.CharField(widget=SummernoteInplaceWidget)
    document = forms.CharField(widget=SummernoteInplaceWidget)
