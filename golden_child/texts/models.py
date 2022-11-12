from django.db import models
#from users.models import ParentUser, ChildUser
from django.utils import timezone
# Create your models here.


class parent_question(models.Model):
    content = models.CharField(max_length=150)  # question
    create_date = models.DateTimeField(default=timezone.now)

    '''def __str__(self):
        return self.content'''

class child_answer(models.Model):
    question = models.OneToOneField(parent_question, null=False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()  # answer
    # parent_id = ParentUser.id
    create_date = models.DateTimeField(default=timezone.now)

    '''def __str__(self):
        return self.content'''
