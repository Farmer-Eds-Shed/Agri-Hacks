from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import About
from .forms import FeedbackForm
from django.contrib import messages


def about(request):
    """
    Renders the About page
    """
    about_list = About.objects.all().order_by('order')

    return render(
        request,
        "about/about.html",
        {"about_list": about_list},
    )


def feedback(request):
    """
    Renders the Feedback page
    """
    if request.method == "POST":
        feedback_form = FeedbackForm(request.POST)

        if feedback_form.is_valid():
            feedback_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Request received! We endeavour to respond within 2 working days.")
            return HttpResponseRedirect('feedback')
    else:
        feedback_form = FeedbackForm()

    return render(
        request,
        "about/feedback.html",
        {
            "feedback_form": feedback_form
        },
    )
