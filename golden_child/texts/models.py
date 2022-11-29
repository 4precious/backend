from django.db import models
from users.models import User
#from django.utils import timezone
# Create your models here.


class Question(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)

    # @property
    # def get_email(self):
    #     return self.user.email


class Answer(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.OneToOneField(
        Question, null=False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()
    # analysis_result = models.CharField(max_length=150, editable=False, default='')
    result_happiness = models.FloatField(editable=False, default=0.00)
    result_anxiety = models.FloatField(editable=False, default=0.00)
    result_embarrassment = models.FloatField(editable=False, default=0.00)
    result_sadness = models.FloatField(editable=False, default=0.00)
    result_anger = models.FloatField(editable=False, default=0.00)
    result_injury = models.FloatField(editable=False, default=0.00)

    @property
    def get_content(self):
        return self.content

    # @property
    # def get_email(self):
    #     return self.user.email
