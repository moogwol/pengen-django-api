from django.db import models

class Drawing(models.Model):
    title = models.CharField(max_length=100)
    dataURL = models.TextField()

    def __str__(self):
        return self.title
