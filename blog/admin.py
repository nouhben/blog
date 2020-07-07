from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Reaction, Reply
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reaction)
admin.site.register(Reply)