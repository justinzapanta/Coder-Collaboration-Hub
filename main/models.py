from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=250)
    project_description = models.CharField(max_length=500)
    project_discord_link = models.TextField()
    project_github_link = models.TextField
    project_date = models.CharField(max_length=250)

    def __str__ (self):
        return self.project_name
    