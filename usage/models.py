from django.db import models
from django.core.urlresolvers import reverse

class UseCase(models.Model):
	file_to_convert = models.FileField()

	def __str__(self):
		return self.file_to_convert.url

	def get_absolute_url(self):
		return reverse('usage:convertor', kwargs={'file_id' : self.pk})