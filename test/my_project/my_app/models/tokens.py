from django.db import models

class Tokens(models.Model):
    token = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"