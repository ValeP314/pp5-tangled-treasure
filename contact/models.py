from django.db import models
from datetime import datetime


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_message = models.TextField()
    contact_submitted_on = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['-contact_submitted_on']

    def __str__(self):
        return self.contact_name
