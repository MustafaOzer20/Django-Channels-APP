from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Channels(models.Model):
    title = models.CharField(max_length=100)
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_channels')
    is_private = models.BooleanField(default=False)
    users = models.ManyToManyField(User, through='ChannelsMembership', related_name='member_channels')   
    created_at = models.DateTimeField(auto_now_add=True)

class ChannelMessages(models.Model):
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ChannelsMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

class ChannelJoinRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

