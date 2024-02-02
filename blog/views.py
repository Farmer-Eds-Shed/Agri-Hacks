from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from .forms import PostForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

# Blog List View
class PostList(generic.ListView):
    queryset = Post.objects.all().filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


# Loged in Users Blog List
class MyPosts(generic.ListView):
    template_name = "blog/index.html"
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.all().filter(author=self.request.user)


# Detailed Post View
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.count()
     
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

def post_like(request, slug):
    if request.method == "POST":
        instance = Post.objects.get(slug=slug)
        if not instance.likes.filter(id=request.user.id).exists():
            instance.likes.add(request.user)
            instance.save() 
            return render( request, 'blog/likes_area.html', context={'post':instance})
        else:
            instance.likes.remove(request.user)
            instance.save() 
            return render( request, 'blog/likes_area.html', context={'post':instance})

# New Post View
@login_required(login_url="/accounts/login/")
def post_create(request):

    if request.method == "POST":
        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            fs= post_form.save(commit=False)
            fs.author= request.user
            fs.save()
            messages.add_message(request, messages.SUCCESS, "post created")
            return HttpResponseRedirect(reverse('post_detail', args=[fs.slug]))

    post_form = PostForm()

    return render(
        request,
        "blog/post_edit.html",
        {
            "post_form": post_form
        },
    )


# Edit Post View
@login_required(login_url="/accounts/login/")
def post_edit(request, slug):
    
    context ={}
    queryset = Post.objects
    post = get_object_or_404(queryset, slug = slug)
    post_form = PostForm(request.POST or None, instance = post)
    
    if request.user!=post.author:
       messages.add_message(request, messages.INFO, "Not uthorized to edit that post")
       return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    
    if post_form.is_valid():
        fs= post_form.save(commit=False)
        fs.save()
        messages.add_message(request, messages.SUCCESS, "post Updated")
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    context["post_form"] = post_form
    return render(request, "blog/post_edit.html", context)


# DeletePost View
@login_required(login_url="/accounts/login/")
def post_delete(request, slug):
    
    queryset = Post.objects
    post = get_object_or_404(queryset, slug = slug)
    context = {'post': post}
    
    if request.user==post.author: 

        if request.method == 'GET':
            return render(request, 'blog/confirm_delete.html',context)
        
        elif request.method == 'POST':
            post.delete()
            messages.success(request,  'The post has been deleted successfully.')
            return HttpResponseRedirect('home')
        



# Edit Comments View    
@login_required(login_url="/accounts/login/")
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Delete Comments View
@login_required(login_url="/accounts/login/")
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))