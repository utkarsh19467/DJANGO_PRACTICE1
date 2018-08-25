from django.contrib import admin
from home.models import Friend
from home.models import Post
# Register your models here.
admin.site.register(Post)
admin.site.register(Friend)