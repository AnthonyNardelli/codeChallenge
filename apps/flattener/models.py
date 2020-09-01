from django.db import models

# Create your models here.
class Results(models.Model):
    data = models.TextField(max_length=255)

    def __str__(self):
        return str(self.data)
