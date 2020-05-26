from django.db import models

# Create your models here.

class Point(models.Model):
    x = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{}".format(self.x)
