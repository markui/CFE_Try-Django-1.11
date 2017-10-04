from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
	name 			= models.CharField(max_length=120)
	location 		= models.CharField(max_length=120, blank=True)
	category 		= models.CharField(max_length=120, blank=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	slug			= models.SlugField(unique=True)
	# my_date_field 	= models.DateTimeField()

	def __str__(self):
		return self.name
	
	@property
	def title(self):
		return self.name
		


