from django import forms
from .models import Stdproject

class RegistrationForm(forms.Form):
	#name = forms.CharField(required=False)
	email = forms.EmailField()
	phone = forms.IntegerField()
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

class StdprojectForm(forms.ModelForm):
	class Meta:
		model = Stdproject
		fields = ["email", "phone", "professional", "project_topic", "abstract", "country",]
	
