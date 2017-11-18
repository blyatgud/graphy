from __future__ import unicode_literals
from django.db import models

class Graphy(models.Model):

	nome = models.CharField(max_length=100)
	ano = models.CharField(max_length=100)
	grupo = models.CharField(max_length=100)
	genero = models.CharField(max_length=100)
	img_url = models.CharField(max_length=100)

	def __str__(self):
		return self.nome