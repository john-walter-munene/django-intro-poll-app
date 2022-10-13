from django.utils import timezone
from django.db import models
import datetime

# Create your models here.

class Question(models.Model):
    """Creates the question, additional features like date included."""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        """Creating a better reprsentation of our objects"""
        return self.question_text
    
    def was_published_recently(self):
        """Recently published question"""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    
class Choice(models.Model):
    """The Choices and Tallying votes."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        """Create a better visual impression"""
        return self.choice_text
    