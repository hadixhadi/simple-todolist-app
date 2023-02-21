from django.db import models

# Create your models here.
class Todos(models.Model):
    title=models.CharField(max_length=250)
    is_done=models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}".format(self.title,self.is_done)