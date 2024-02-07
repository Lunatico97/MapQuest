from django.db import models

# Create your models here.
class Participant(models.Model):
	name = models.CharField(max_length=30) ;
	age = models.IntegerField() ;
	bio = models.TextField(max_length=200, default='') ;
	
	def __str__(self):
		return self.name ;
