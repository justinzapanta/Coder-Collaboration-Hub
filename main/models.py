from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class User_UUID(models.Model):
    user_UIID = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    user_account = models.ForeignKey(User, on_delete=models.CASCADE)

class Projects(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=250)
    project_description = models.TextField()
    project_tools = models.CharField(max_length=250)
    project_discord_link = models.TextField()
    project_github_link = models.TextField()
    search_reference = models.TextField()
    project_image = models.ImageField(upload_to='./main/static/img/project_img', default=None, null=True)
    project_date = models.CharField(max_length=250)

    def __str__ (self):
        return self.project_name


class Favorites(models.Model):
    favorite_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    favorite_project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class User_Friends(models.Model):
    friend_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    user_friend_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    