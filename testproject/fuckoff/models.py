from django.db import models

# Create your models here.
class fuckoff(models.Model):
    title = models.CharField(max_length=50)   # The max lenght is reqiured
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=22,)
    summary = models.TextField(blank=False, null=False)
    feature = models.BooleanField(default=True)