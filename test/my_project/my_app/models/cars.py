from django.db import models

class Cars(models.Model):
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    date =  models.DateField()

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"
