from django.contrib import admin
from .models import Petition

# Register your models here.
class PetitionAdmin(admin.ModelAdmin):
	exclude = ('aadhar', 'pan', 'photo', 'petitioners', 'complainees')
	readonly_fields = ('aadhar_tag', 'pan_tag', 'photo_tag')

admin.site.register(Petition, PetitionAdmin)
