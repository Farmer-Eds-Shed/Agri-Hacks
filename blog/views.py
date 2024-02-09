from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.db.models import Q


# Create your views here.

# Blog List View
class PostList(generic.ListView):
    queryset = Post.objects.all().filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6
    page_title = "Most Recent"

    def get_context_data(self):
        data = super(PostList, self).get_context_data()
        data['page_title'] = 'Latest Posts'
        return data


# Loged in Users Blog List
class MyPosts(generic.ListView):
    template_name = "blog/index.html"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.all().filter(author=self.request.user)

    def get_context_data(self):
        data = super(MyPosts, self).get_context_data()
        data['page_title'] = str(self.request.user) + "'s Posts"
        return data


# Loged in Users Blog Draft List
class MyPostsDraft(generic.ListView):
    template_name = "blog/index.html"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.all().filter(author=self.request.user).filter(status=0)

    def get_context_data(self):
        data = super(MyPostsDraft, self).get_context_data()
        data['page_title'] = str(self.request.user) + "'s Draft Posts"
        return data


# Loged in Users Published Blog List
class MyPostsPublished(generic.ListView):
    template_name = "blog/index.html"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.all().filter(author=self.request.user).filter(status=1)

    def get_context_data(self):
        data = super(MyPostsPublished, self).get_context_data()
        data['page_title'] = str(self.request.user) + "'s Published Posts"
        return data


# Search View
class Search(generic.ListView):
    template_name = "blog/index.html"
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get("query")
        if query is not None:
            return Post.objects.filter(Q(title__icontains=query)
                                       | Q(author__username__icontains=query)
                                       | Q(category__name__icontains=query)).filter(status=1)
        else:
            return Post.objects.all().filter(status=1)

    def get_context_data(self):
        query = self.request.GET.get("query")
        data = super(Search, self).get_context_data()
        data['page_title'] = 'Search Results: ' + '"' + str(query) + '"'
        return data


# Category View
def category_view(request, category):
    post_list = Post.objects.filter(category=category).filter(status=1)
    page_category = Category.objects.get(pk=category)
    page_title = page_category.name
    return render(request, "blog/index.html",
                  {'post_list': post_list, 'page_title': page_title})


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


# Post Like View
@login_required(login_url="/accounts/login/")
def post_like(request, slug):
    instance = Post.objects.get(slug=slug)
    if request.method == "POST":
        if not instance.likes.filter(id=request.user.id).exists():
            instance.likes.add(request.user)
            instance.save()
            return render(request, 'blog/likes_area.html',
                          context={'post': instance})
        else:
            instance.likes.remove(request.user)
            instance.save()
            return render(request, 'blog/likes_area.html',
                          context={'post': instance})
    else:
        instance.save()
        return render(request, 'blog/likes_area.html',
                      context={'post': instance})


# Made One View
@login_required(login_url="/accounts/login/")
def made_one(request, slug):
    instance = Post.objects.get(slug=slug)
    if request.method == "POST" and request.user.is_authenticated:
        if not instance.made_one.filter(id=request.user.id).exists():
            instance.made_one.add(request.user)
            instance.save()
            return render(request, 'blog/likes_area.html',
                          context={'post': instance})
        else:
            instance.made_one.remove(request.user)
            instance.save()
            return render(request, 'blog/likes_area.html',
                          context={'post': instance})
    else:
        instance.save()
        return render(request, 'blog/likes_area.html',
                      context={'post': instance})


# New Post View
@login_required(login_url="/accounts/login/")
def post_create(request):

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            fs = post_form.save(commit=False)
            fs.author = request.user
            fs.save()
            messages.add_message(request, messages.SUCCESS, "post created")
            return HttpResponseRedirect(reverse('post_detail', args=[fs.slug]))
    else:
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

    context = {}
    queryset = Post.objects
    post = get_object_or_404(queryset, slug=slug)
    post_form = PostForm(request.POST or None, request.FILES or None,
                         instance=post)

    if request.user != post.author:
        messages.add_message(request, messages.INFO,
                             "Not uthorized to edit that post")
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    if post_form.is_valid():
        fs = post_form.save(commit=False)
        fs.save()
        messages.add_message(request, messages.SUCCESS, "post Updated")
        return HttpResponseRedirect(reverse('post_detail', args=[fs.slug]))

    context["post_form"] = post_form
    return render(request, "blog/post_edit.html", context)


# DeletePost View
@login_required(login_url="/accounts/login/")
def post_delete(request, slug):

    queryset = Post.objects
    post = get_object_or_404(queryset, slug=slug)
    context = {'post': post}

    if request.user == post.author:

        if request.method == 'GET':
            return render(request, 'blog/confirm_delete.html', context)

        elif request.method == 'POST':
            post.delete()
            messages.success(request,
                             'The post has been deleted successfully.')
            return HttpResponseRedirect('/')


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
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

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
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
