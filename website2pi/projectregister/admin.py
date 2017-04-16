from django.contrib import admin

# Register your models here.
from .models import Stdproject

class StdprojectAdmin(admin.ModelAdmin):
	class Meta:
		model = Stdproject

admin.site.register(Stdproject, StdprojectAdmin)
