from random import choice
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date  = models.DateTimeField(verbose_name="date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self) -> bool:
        one_day =  datetime.timedelta(days=1)
        today = timezone.now()
        return today - one_day <= self.pub_date

class Choice(models.Model):
    id_questions = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text
