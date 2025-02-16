from django.contrib import admin
from .models import Application

# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
	exclude = ('aadhar', 'pan', 'driving_license', 'voter_id', 'photo', 'members', 'elicense')
	readonly_fields = ('aadhar_tag', 'pan_tag', 'driving_license_tag', 'voter_id_tag', 'photo_tag')

admin.site.register(Application, ApplicationAdmin)
