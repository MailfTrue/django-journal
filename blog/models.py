from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
user = User.objects.all()[0].username
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.CharField(max_length=len(user),default=user,editable=False)
    title = models.CharField(max_length=200)
    sticky = models.BooleanField(default=False, verbose_name = "Sticky", help_text="If checked this post will appear on top of list")
    text = models.TextField()

    categories = models.ManyToManyField(Category)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def is_sticky(self):
        return self.sticky



    def __str__(self):
        return self.title
