from django.shortcuts import render
from .models import About


def about_me(request):
    """
    Renders the About page
    """
    about_list = About.objects.all().order_by('-updated_on')

    return render(
        request,
        "about/about.html",
        {"about_list": about_list},
    )
