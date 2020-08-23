from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
