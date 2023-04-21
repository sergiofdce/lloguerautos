from django.db import models



class Automobil(models.Model):
	marca = models.CharField(max_length=50)
	model = models.CharField(max_length=50)
	matricula = models.CharField(max_length=10)


