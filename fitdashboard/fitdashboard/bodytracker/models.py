from django.db import models

# Create your models here.
class WeightRecords(models.Model):
    """
    体重记录的model
    """
    id = models.AutoField(primary_key=True)
    weight = models.FloatField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ["-date"]
    
    def __str__(self):
        return '%s: %skg' % (self.date.date(), self.weight)
