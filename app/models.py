import re
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


ARTICLE_STATUS = (
    ("draft", "draft"),
    ("inprogress", "in progress"),
    ("published", "published"))


class UserProfile(AbstractUser):
    pass

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default="")
    word_count = models.IntegerField(blank=True, default=0)
    twitter_post = models.TextField(blank=True, default="")
    status = models.CharField(max_length=30, choices=ARTICLE_STATUS, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # #save model method
    # def save(self, *args, **kwargs):
    #     text = re.sub(r"<[^>]*", "", self.content).replace("&nbsp;", " ")
    #     self.word_count = len(re.findall(r"\b\w+\b", text))

    #     super().save(*args, **kwargs)
    '''We call the original save() method (super() refers to the parent class, models.Model).
        Our object is saved to the database, and we maintain the default behavior of Django.'''

 #save model method
    def save(self, *args, **kwargs):
        self.word_count = len(self.content.split()) #word_count
        super().save(*args, **kwargs) #save to the database 
