from .models import Post, Comment, Category
from django import forms
from django_summernote.widgets import SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', "category", 'featured_image',
                  'concept', 'document', 'status']
    concept = forms.CharField(widget=SummernoteInplaceWidget, label="Project Description:")
    document = forms.CharField(widget=SummernoteInplaceWidget, label="Build Details:")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
 