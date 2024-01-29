from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all().filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post
        },
    )

@login_required(login_url="/accounts/login/")
def post_create(request):

    if request.method == "POST":
        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            fs= post_form.save(commit=False)
            fs.author= request.user
            fs.save()
            messages.add_message(request, messages.SUCCESS, "post created")
            return redirect("/"+fs.slug)

    post_form = PostForm()

    return render(
        request,
        "blog/post_create.html",
        {
            "post_form": post_form
        },
    )

@login_required(login_url="/accounts/login/")
def post_edit(request, slug):
    
    context ={}
    queryset = Post.objects
    post = get_object_or_404(queryset, slug = slug)
    form = PostForm(request.POST or None, instance = post)
    
    if request.user!=post.author:
       messages.add_message(request, messages.INFO, "Not uthorized to edit that post")
       return redirect("/"+slug)
    
    if form.is_valid():
        fs= form.save(commit=False)
        fs.save()
        messages.add_message(request, messages.SUCCESS, "post Updated")
        return redirect("/"+fs.slug)

    context["form"] = form
    return render(request, "blog/post_edit.html", context)


