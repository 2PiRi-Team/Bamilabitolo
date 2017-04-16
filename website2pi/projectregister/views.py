#stdproject views
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, Http404
from .forms import RegistrationForm, ProjectregisterForm
from .models import Stdproject
#from django.http import HttpResponse

# Create your views here.

#this is to get nthe user's ip address
def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FRO")
		if x_forward:		
			ip = x_forward.split(",")[0]	
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return  ip	



#####TO GET A REFERENCE NUMBER FOR EACH USER####
#str(user_id)[:11].replace('-', '').lower()
import uuid


 
def get_ref_id():
	ref_id = str(uuid.uuid4())[:15].replace('-', '').lower()
	try:
		id_exist = Projectregister.objects.get(ref_id =ref_id)
		get_ref_id()
	except:
		return ref_id


##To Share the page 01 ##

def notifyme(request, ref_id):	
	try:	
		projectregister_obj = Projectregister.objects.get(ref_id=ref_id)
		friends_referred = Projectregister.objects.filter(friend=projectregister_obj)
		count = projectregister_obj.referral.all().count()
		ref_url = settings.SHARE_URL + str(projectregister_obj.ref_id)
		context = {"ref_url": ref_url, "ref_id": projectregister_obj.ref_id, "count": count}	
		template = "notifyme.html" 
		return render(request, template, context)
	except:
		raise Http404

'''
##To Share the page 02 ##

def notifyme(request, ref_id):	
	context = {"ref_id": ref_id}
	template = "notifyme.html" 
	return render(request, template, context)
'''




##ComingSoon##
# This is using model forms
def projectregister(request):	
	try:           
		projectregister_id = request.session['projectregister_id_ref']
		obj = Projectregister.objects.get(id=projectregister_id)		
	except:
	 	 obj = None

	
	form = ProjectregisterForm(request.POST or None)
	if form.is_valid():
		new_projectregister = form.save(commit=False)
	#WE might do something here
		email = form.cleaned_data['email'] 
 		new_projectregister_old, created = Projectregister.objects.get_or_create(email=email)
		if created:
			new_projectregister_old.ref_id = get_ref_id()
		#ADD A FRIEND WHO REFERRED US TO OUR projectregister MODEL OR A RELATED ONE.
			if not obj == None:
			   new_projectregister_old.friend = obj
			new_projectregister_old.ip_address = get_ip(request)
			new_projectregister_old.save()
		
		#PRINTING OF FRIENDS THAT JOINED AS A RESULT OF A SHARE#
			print Projectregister.objects.filter(friend=obj)
			#print obj.referral.all()
		##redirect here##
			return HttpResponseRedirect("%s" %(new_projectregister_old.ref_id))
#This is using normal django forms
#	form = EmailForm(request.POST or None)
#	if form.is_valid():
#		email = form.cleaned_data['email']
#		new_notify_me, created = Comingsoon.objects.get_or_create(email=email)		
#		if created:
#			print "Email Sucessfully Added"
#		else:	print "Sorry, Email already exists"

	#redirect here
		#new_comingsoon.ip_address = get_ip(request)
		#new_comingsoon.save()
	context = {"form": form}
	template = "reg_project.html" 
	return render(request, template, context)




