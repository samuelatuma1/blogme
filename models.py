from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        #super gives this class access to the proceeding parent method 
        # in this case, get_queryset
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    objects=models.Manager()
    published = PublishedManager()
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, 
                            unique_for_date='publish')

    author = models.ForeignKey(User, 
                                on_delete=models.CASCADE,
                                 related_name='blog_posts')
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)

    #set the field to now when the object is first created
    created = models.DateTimeField(auto_now_add=True) 
    #Automatically set the field to now every time the object is saved
    updated = models.DateTimeField(auto_now=True) 

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        return reverse(
            'blog:post_detail', args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )

    class Meta:
        ordering = ('-publish',)
        

    def __str__(self):
        return self.title