from django.db import models ;
from django.core.validators import MaxValueValidator, MinValueValidator ;

# Create your models here.
class Lobby(models.Model):
	name = models.CharField(max_length=15) ;
	secret_key = models.CharField(max_length=6) ;
	purpose = models.TextField(max_length=200, default='') ;
	count = models.IntegerField(default=0, validators=[ MaxValueValidator(25), MinValueValidator(0) ]) ;
	
	def __str__(self):
		return self.name ;

class Participant(models.Model):
	name = models.CharField(max_length=30) ;
	age = models.IntegerField() ;
	bio = models.TextField(max_length=200, default='') ;
	lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE) ;
	
	def __str__(self):
		return self.name ;
