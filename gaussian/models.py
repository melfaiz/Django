from django.db import models

# Create your models here.

class Point(models.Model):
    x = models.DecimalField(max_digits=5, decimal_places=2)
    y = models.DecimalField(max_digits=5, decimal_places=2)
    t = models.TimeField(auto_now=True)

    def __str__(self):
        return "{}({},{})".format(self.t,self.x, self.y)