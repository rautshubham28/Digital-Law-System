from djongo import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from base64 import b64encode

# Create your models here.
class Member(models.Model):
	member = models.TextField()
	class Meta:
		abstract = True

class Application(models.Model):
	user = models.ForeignKey(to=User, on_delete=models.CASCADE)
	name = models.TextField()
	mobile = models.BigIntegerField()
	email = models.EmailField()
	address = models.TextField(blank=True)
	age = models.SmallIntegerField(blank=True)
	gender = models.TextField(blank=True)
	annual_income = models.IntegerField(blank=True)
	members = models.ArrayField(Member, blank=True)
	source = models.TextField(blank=True)
	destination = models.TextField(blank=True)
	reason = models.TextField(blank=True)
	vehicle = models.TextField(blank=True)
	duration = models.IntegerField(blank=True)
	photo = models.TextField()
	aadhar = models.TextField(blank=True)
	pan = models.TextField(blank=True)
	driving_license = models.TextField(blank=True)
	voter_id = models.TextField(blank=True)
	application_type = models.TextField()
	is_approved = models.BooleanField(default=False)
	elicense = models.TextField()
	application_date = models.DateTimeField(auto_now_add=True, editable=False)

	def photo_tag(self):
		return mark_safe('<img src = "data: image/png; base64, {}" width="250" height="250">'.format(self.photo))
	
	def aadhar_tag(self):
		return mark_safe('<img src = "data: image/png; base64, {}" width="500" height="250">'.format(self.aadhar))
	
	def pan_tag(self):
		return mark_safe('<img src = "data: image/png; base64, {}" width="500" height="250">'.format(self.pan))

	def driving_license_tag(self):
		return mark_safe('<img src = "data: image/png; base64, {}" width="500" height="250">'.format(self.driving_license))

	def voter_id_tag(self):
		return mark_safe('<img src = "data: image/png; base64, {}" width="250" height="500">'.format(self.voter_id))

	photo_tag.short_description = 'Photo'
	photo_tag.allow_tags = True
	aadhar_tag.short_description = 'Aadhar'
	aadhar_tag.allow_tags = True
	pan_tag.short_description = 'Pan'
	pan_tag.allow_tags = True
	driving_license_tag.short_description = 'Driving License'
	driving_license_tag.allow_tags = True
	voter_id_tag.short_description = 'Voter ID'
	voter_id_tag.allow_tags = True

