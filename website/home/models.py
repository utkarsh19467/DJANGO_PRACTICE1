from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    post=models.CharField(max_length=500)
    user=models.ForeignKey(User)


class Friend(models.Model):
    users=models.ManyToManyField(User,related_name='friend_set')
    current_user=models.ForeignKey(User,related_name='owner',null=True)

    @classmethod
    def make_friend(cls,current_user,new_friend):
        friend,created=cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend) 

    @classmethod
    def lose_friend(cls,current_user,new_friend):
        friend,created=cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend) 
