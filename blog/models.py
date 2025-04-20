from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200,)
    slug = AutoSlugField(populate_from='title', editable=True,
                         always_update=True, unique=True)
    category = models.ForeignKey(Category, related_name="posts",
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    concept = models.TextField(verbose_name = "Product Description:")
    document = models.TextField(verbose_name = "Build Details")
    created_on = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='user_like', blank=True)
    made_one = models.ManyToManyField(User, related_name='made_one',
                                      blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_made(self):
        return self.made_one.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.author} commented | {self.body} --> {self.post}"
