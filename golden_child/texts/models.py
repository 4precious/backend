from django.db import models
from users.models import User
#from django.utils import timezone
# Create your models here.


class parent_question(models.Model):
    # if User.is_parent != True:
    #     raise ValueError('Question should be made by parent user')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)  # question
    create_date = models.DateTimeField(auto_now_add=True)

    '''def __str__(self):
        return self.content'''

class child_answer(models.Model):
    # if (User.is_child != True):
    #     raise ValueError('Answer should be made by child user')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.OneToOneField(parent_question, null=False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    '''def __str__(self):
        return self.content'''
