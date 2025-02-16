from djongo import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from base64 import b64encode

# Create your models here.
class Petitioner(models.Model):
	petitioner = models.TextField()
	class Meta:
		abstract = True

class Complainee(models.Model):
	complainee = models.TextField()
	class Meta:
		abstract = True

class Petition(models.Model):
	user = models.ForeignKey(to=User, on_delete=models.CASCADE)
	title = models.TextField()
	state = models.TextField(blank=True)
	district = models.TextField(blank=True)
	description = models.TextField()
	petitioners = models.ArrayField(Petitioner)
	complainees = models.ArrayField(Complainee)
	court = models.TextField()
	hearing = models.DateField(blank=True, null=True)
	result = models.BooleanField(blank=True)
	photo = models.TextField()
	aadhar = models.TextField()
	pan = models.TextField()

	def photo_tag(self):
		return mark_safe('<img src = "data: image/png; base64, {}" width="250" height="250">'.format(self.photo))
	
	def aadhar_tag(self):
		return mark_safe('<img src = "data: image/png; base64, {}" width="500" height="250">'.format(self.aadhar))
	
	def pan_tag(self):
		return mark_safe('<img src = "data: image/png; base64, {}" width="500" height="250">'.format(self.pan))

	photo_tag.short_description = 'Photo'
	photo_tag.allow_tags = True
	aadhar_tag.short_description = 'Aadhar'
	aadhar_tag.allow_tags = True
	pan_tag.short_description = 'Pan'
	pan_tag.allow_tags = True
