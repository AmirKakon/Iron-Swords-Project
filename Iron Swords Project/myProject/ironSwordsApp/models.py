from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# ironSwordsApp/models.py

class Hero(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    hometown = models.CharField(max_length=100)
    country_of_birth = models.CharField(max_length=100)
    hero_story = models.TextField()
    image = models.ImageField(upload_to='heroes_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class KibbutzStory(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class NovaPartyTestimony(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    owner = models.CharField(max_length=255)
    story = models.TextField()


    def __str__(self):
        if self.author== None:
            return ''
        else:
            return self.author.username
    
class Testimonial(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    story = models.TextField()

    def __str__(self):
        return self.author.username
    

class AbducteeTestimony(models.Model):
    owner = models.CharField(max_length=100)
    story = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()
    date_of_return = models.DateField()
    image = models.ImageField(upload_to='testimonies/', blank=True, null=True)  # Ensure this field is present


    def __str__(self):
        return self.owner  
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User who made the comment.
    content = models.TextField()  # Content of the comment.
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the comment was created.
    video_url = models.URLField(blank=True, null=True)  # Optional URL for a video related to the comment.

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['created_at']

class Candle(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    date_lit = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} lit a candle on {self.date_lit.strftime('%Y-%m-%d')}."