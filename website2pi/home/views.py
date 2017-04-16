#home views
from django.shortcuts import render

# Create your views here.

def homepage(request):
	context = {} 
	template = "homepage.html" 
	return render(request, template, context)
