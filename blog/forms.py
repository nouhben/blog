from django import forms
from django.contrib.auth.models import User
from blog.models import Post, Comment, Reply, Reaction

class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content', 'comment_image']