from django.db import models
from users.models import ParentUser, ChildUser
from django.utils import timezone
# Create your models here.


class ParentText(models.Model):
    content = models.CharField(max_length=150)  # question
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class ChildText(models.Model):
    content = models.CharField(max_length=150)  # answer
    # parent_id = ParentUser.id
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
