from django.db import models

# Create your models here.

class Todo(models.Model):
    task_name=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    user=models.CharField(max_length=120)

    def __str__(self):
        return self.task_name
