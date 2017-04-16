from django import forms
from .models import Stdproject

class RegistrationForm(forms.Form):
	#name = forms.CharField(required=False)
	email = forms.EmailField()
	phone = forms.IntegerField()
	city = forms.CharField()
	post_code = forms.IntegerField()
	professional = (
    ('Enr', 'Engineering'),
    ('Compt Sci', 'Computer Science'),    
	)
	project_topic = forms.CharField()
	abstract = forms.CharField()
	country = (
    ('Nig', 'Nigeria'),
    ('Gh', 'Ghana'),    
	)

class ProjectregisterForm(forms.ModelForm):
	class Meta:
		model = Stdproject
		fields = ["email", "phone", "city", "post_code", "professional",  "project_topic", "abstract", "country",]
	
