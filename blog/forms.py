from .models import Post
from .models import Comment
from django import forms
from django_summernote.widgets import SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','featured_image','concept','document','status')
    concept = forms.CharField(widget=SummernoteInplaceWidget)
    document = forms.CharField(widget=SummernoteInplaceWidget)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)