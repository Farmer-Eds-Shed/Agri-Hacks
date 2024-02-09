from .models import Feedback
from django import forms


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('issue','name', 'email', 'message')
