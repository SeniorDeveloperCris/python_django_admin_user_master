from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-created_at', )
