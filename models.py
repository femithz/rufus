from django.db import models

# Create your models here.
class Job(models.Model):

	project = models.CharField(max_length=200, default='DEFAULT VALUE')
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)

class Front(models.Model):

	words = models.CharField(max_length=200, default='DEFAULT VALUE')
	image = models.ImageField(upload_to='images/')
	

