from . import views
from django.urls import path


urlpatterns = [
    path('', views.about, name='about'),
    path('feedback', views.feedback, name='feedback'),
]