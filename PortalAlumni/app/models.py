

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
# Create your models here.

class SignUpModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=255,blank=False,unique=True)
    graduation_year = models.DateTimeField(blank=False)
    def __str__(self):
        return self.user.username


class PostModel(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE,default=0)
    title = models.CharField(max_length=255)
    info = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})


class EventModel(models.Model):
    user = models.ForeignKey(User,related_name='events',on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    photo=models.ImageField(null=True,upload_to='event_pics/',blank=True)
    text=models.TextField()
    published_date=models.DateTimeField(default=timezone.now)
    number_of_comments=models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('event_detail',kwargs={'pk':self.pk})

class EventComment(models.Model):
    event = models.ForeignKey(EventModel,related_name='event_comment',on_delete=models.CASCADE,default=0)
    name=models.CharField(max_length=255)
    comment=models.TextField()
    published_date_comment=models.DateTimeField(default=timezone.now)


