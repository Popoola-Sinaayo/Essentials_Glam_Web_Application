from django.db import models

# Create your models here.


class Mail_Subscriber(models.Model):
    Email_Subscribers = models.EmailField(max_length=400, unique=True)

    def __str__(self):
        return f"{self.Email_Subscribers}"


class Comment(models.Model):
    User = models.CharField(max_length=1000)
    User_Email = models.EmailField(max_length=1000)
    comment = models.CharField(max_length=1000000)

    def __str__(self):
        return f"User:{self.User}, Email:{self.User_Email}, Comment:{self.comment}"


class blog(models.Model):
    Title = models.CharField(max_length=100000)
    Category = models.CharField(max_length=10000, default='Fashion')
    Date = models.DateTimeField(auto_now_add=True)
