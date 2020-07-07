from django.db import models
from django.utils import timezone
#to get the user model
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    class Meta:
        ordering = ['-date_posted']
    def __str__(self):
        return f'{self.title} By {self.author}'
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(default=timezone.now)
    comment_content = models.TextField(null=False, blank=False)
    has_reply = models.BooleanField(default=False)
    #reply_to = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment_author} commented this on post by {self.post.author}'
    
class Reply(models.Model):
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(Comment,on_delete=models.CASCADE)
    reply_author = models.OneToOneField(User, on_delete=models.CASCADE)
    date_replied = models.DateTimeField(default=timezone.now)
    reply_content = models.TextField(null=False, blank=False)
    

    def __str__(self):
        return f'{self.reply_author} replied to the comment {self.reply_to}'
    

class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction_author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_reacted = models.DateTimeField(default=timezone.now)
    reactions = [
        ('Love','Love'),
        ('Like','Like'),
        ('Dislike','Dislike'),
        ('Animal','Animal'),
    ]
    reaction_type = models.CharField(max_length=50, choices=reactions)
