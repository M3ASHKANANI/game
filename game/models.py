from django.db import models

class Game(models.Model):
	name = models.CharField(max_length=220)
	release_date = models.DateField()
	platforms = models.CharField(max_length=220, null=True)
	multiplayer = models.BooleanField()
	image = models.ImageField ()


def __str__(self):
	return self.name
