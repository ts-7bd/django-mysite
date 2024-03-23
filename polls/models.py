"""
Two models are defined here: Question and Choice. 
    A Question has a question and a publication date. 
    A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.
"""

from django.contrib import admin
from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    # by default sorting by the output of an arbitrary method is not supported
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
        
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
    # object representation
    def __str__(self):
        #return f"Question(pk={self.pk}, text='{self.question_text}', pub_date={self.pub_date})"
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text