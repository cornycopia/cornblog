from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Entry(models.Model):
    pub_date = models.DateTimeField('Date of Publication')
    title = models.CharField('Title',max_length=100)
    entry_text = models.TextField('Entry Text')
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Time of Publication')
    commenter = models.CharField('Commenter',max_length=100)
    comment_text = models.TextField('Comment')
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.commenter + ':' + self.comment_text
