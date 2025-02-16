from djongo import models
from django.contrib.auth.models import User

# Create your models here.
class Lawyer(models.Model):
	user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='lawyer_profile')
	domain = models.TextField()
	mobile = models.BigIntegerField()
	years_of_experience = models.SmallIntegerField()
	state = models.TextField()

class Message(models.Model):
    sender = models.BooleanField()                                      # True: Client, False: Lawyer
    message = models.TextField()
    class Meta:
        abstract = True

class Connect(models.Model):
    client = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='client')
    lawyer = models.ForeignKey(to=Lawyer, on_delete=models.CASCADE, related_name='lawyer')
    conversation = models.ArrayField(Message)