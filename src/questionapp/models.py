from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question_id = models.ForeignKey("Question", on_delete=models.CASCADE)
    answer = models.CharField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
