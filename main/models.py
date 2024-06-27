from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=250)
    project_description = models.TextField()
    project_tools = models.CharField(max_length=250)
    project_discord_link = models.TextField()
    project_github_link = models.TextField()
    project_date = models.CharField(max_length=250)

    def __str__ (self):
        return self.project_name


class Favorites(models.Model):
    favorite_id = models.AutoField(primary_key=True)
    favorite_project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class User_Friends(models.Model):
    friend_id = models.AutoField(primary_key=True)
    user_friend_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    