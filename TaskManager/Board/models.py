from django.db import models
from users.models import User
# Create your models here.

class Board(models.Model):
    name=models.CharField(max_length=256)
    description=models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='boards')

class Task(models.Model):
    STATUS_CHOICES = (
        ('to-do', 'To-Do'),
        ('in-progress', 'In Progress'),
        ('done', 'Done'),
    )
    title = models.CharField(max_length=255) 
    description = models.TextField(blank=True, null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to-do')
    due_date = models.DateField(null=True, blank=True)
