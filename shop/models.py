from django.db import models

class Product(models.Model):
	title = models.CharField(max_length=100)
	price = models.FloatField(default=1.99)
	discounted_price = models.FloatField()
	category = models.CharField(max_length=100)
	description = models.TextField()
	image = models.CharField(max_length=500)

	def __str__(self):
		return self.title
	
