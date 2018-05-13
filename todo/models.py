from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


STATUS = (('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Done', 'Done'))


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    status = models.CharField(max_length=11, choices=STATUS)

    def get_absolute_url(self):
        return reverse('todo:index')
