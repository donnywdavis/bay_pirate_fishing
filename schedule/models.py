from django.db import models

class Schedule(models.Model):
    event = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    rank = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.event
