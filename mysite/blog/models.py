from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


# Create your models here.
class Post(models.Model):
    #setting up values
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #method for publishing a post and giving it timestamp 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #method to approve comments, 'comments' will be made later on
    #to store user comments on a post 
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    #has to be called get_absolute_url as this is what django looks 
    #for by default
    def get_absolute_url(self):
        #once post is created, go to the details page of the post
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title




class Comment(models.Model):
    #setting up values
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True 
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text 