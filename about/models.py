from django.db import models
from autoslug import AutoSlugField

class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    class Meta:
        verbose_name_plural = "about"
    
    def __str__(self):
        return self.title
    
class Issues(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)
    
    class Meta:
        verbose_name_plural = "issues"
    
    def __str__(self):
        return self.name    
    

class Feedback(models.Model):
    issue= models.ForeignKey(Issues, related_name="feedback_issues",on_delete=models.SET_NULL,blank=True,null=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "feedback"

    def __str__(self):
        return f"{self.issue} request from {self.name}"