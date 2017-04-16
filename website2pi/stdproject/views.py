#std project views
from django.shortcuts import render

# Create your views here.

def stdproject(request):
	context = {} 
	template = "stdproject.html" 
	return render(request, template, context)

