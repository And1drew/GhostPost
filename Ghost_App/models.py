from django.db import models
from datetime import datetime

class BoastOrRoast(models.Model):
    description = models.TextField()
    is_boast = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(default=datetime.now)
    score = models.IntegerField(default = 0)