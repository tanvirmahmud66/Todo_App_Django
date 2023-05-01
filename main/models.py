from django.db import models

# Create your models here.


class TodoModel(models.Model):
    todo = models.TextField(max_length=200)
    is_complete = models.BooleanField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.todo
