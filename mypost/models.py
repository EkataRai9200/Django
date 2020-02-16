from django.db import models

# Create your models here.
class posts(models.Model):
    title=models.charField(max_lenght=100)
    desc=models.TextField()
def __str__ (self):
    return self.title

