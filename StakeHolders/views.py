from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.db.utils import DatabaseError
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.db.models import F
from Applications.models import Application
from Petitions.models import Petition
from .models import Connect, Lawyer
import json

# Create your views here.
def index(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if 'email' in request.POST:
			email = request.POST.get('email')
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			try:
				user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
				citizen = Group.objects.get(name='Citizen') 
				citizen.user_set.add(user)
			except DatabaseError:
				return render(request, 'StakeHolders/index.html', { 'e': 'User already registered, Please Sign In'})
		else:
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				return render(request, 'StakeHolders/index.html', { 'e': 'Invalid Username / Password'})
	else:
		return render(request, 'StakeHolders/index.html', { 'e': '' })

def contact(request):
	return render(request,"StakeHolders/contact.html")

def services(request):
	return render(request,"StakeHolders/services.html")

@login_required
def dashboard(request, page=None):
	if page in [ None, 'applications', 'lawyers', 'clients', 'petitions' ]:
		if request.method == 'POST':
			if page == 'applications':
				delete = request.POST.get('delete')														# For deleting an Application
				Application.objects.filter(pk=delete).delete()
				return redirect('/dashboard/applications')
			if page == 'lawyers' or page == 'clients':
				if 'lawyer_id' in request.POST:															# Client adding a new lawyer
					client = request.user
					lawyer_id = request.POST.get('lawyer_id')
					lawyer = Lawyer.objects.get(pk=lawyer_id)
					connect = Connect.objects.create(client=client, lawyer=lawyer, conversation=[])
					return redirect('/dashboard/lawyers')
				connect = json.loads(request.body)
				if connect['mode'] == 0:																# For Sending Message
					sender = connect['sender']
					message = connect['message']
					conversation_id = connect['conversation_id']
					conversation = Connect.objects.get(pk=conversation_id)
					conversation.conversation.append({ 'sender': sender, 'message': message })
					conversation.save()
					return HttpResponse(True)
				if connect['mode'] == 1:																# For Searching Lawyers
					lawyers = Lawyer.objects.filter(
						domain=connect['domain'],
						years_of_experience__gte=connect['experience'],
						state=connect['state']
					).select_related('user').annotate(first_name=F('user__first_name'), last_name=F('user__last_name'), email=F('user__email'))
					return JsonResponse({ 'lawyers': list(lawyers.values()) })
				if connect['mode'] == 2:																# For Choosing Conversation
					conversation_id = connect['conversation_id']
					conversation = Connect.objects.get(pk=conversation_id)
					return JsonResponse({ 'conversation': conversation.conversation })
			else:
				old = request.POST['old']																# Accept Old and New passwords
				new = request.POST['new']																# from the dashboard form and
				confirm = request.POST['confirm']														# check if the old password is
				if request.user.check_password(old):													# correct. If No, display a
					if new == confirm:																	# message to user. If Yes,
						try:																			# check if New password is
							validate_password(new, request.user)										# same as Confirmation. If No,
							request.user.set_password(new)												# display a message to user.
							request.user.save()															# If Yes, validate the New
							update_session_auth_hash(request, request.user)								# password to make sure it
							message = '<p class="text-success">Password Successfully Updated</p>'		# satisfies the requirements
						except ValidationError:															# of minimum strength of a
							message = '<p class="text-danger">Password too weak! Try again!</p>'		# password. If Not validated,
					else:																				# display a message to user.
						message = '<p class="text-danger">Passwords dont match! Try again!</p>'			# If validated, set the new
				else:																					# password, update user's
					message = '<p class="text-danger">Incorrect Password! Try again!</p>'				# session and inform the user.
				return render(request, 'StakeHolders/dashboard.html', { 'message': message })
		else:
			content = {}
			if page == 'applications':																	# Collect all Applications
				content['applications'] = Application.objects.filter(user_id=request.user)				# submitted by user
			elif page == 'clients':
				if str(request.user.groups.get()) == 'Lawyer':
					content['stakeholders'] = Connect.objects.filter(lawyer=Lawyer.objects.get(user=request.user)).select_related(
						'client').annotate(first_name=F('client__first_name'), last_name=F('client__last_name'))
				else:
					raise Http404()																		# Collect list of connected
			elif page == 'lawyers':																		# lawyers/clients
				if str(request.user.groups.get()) == 'Citizen':
					content['stakeholders'] = Connect.objects.filter(client=request.user).select_related('lawyer').annotate(
						first_name=F('lawyer__user__first_name'), last_name=F('lawyer__user__last_name'), domain=F('lawyer__domain'),
					)
				else:
					raise Http404()
			elif page == 'petitions':
					content['petitions'] = Petition.objects.filter(user=request.user)					# Collect all petitions by user
			else:
				content['applications'] = Application.objects.filter(user_id=request.user).count()		# For getting count of user's
				content['petitions'] = Petition.objects.filter(user=request.user).count()				# Applications, Lawyers/Clients
				if str(request.user.groups.get()) == 'Citizen':											# contacted, Petitions filed.
					content['stakeholders'] = Connect.objects.filter(client=request.user).count()	
				elif str(request.user.groups.get()) == 'Lawyer':
					content['stakeholders'] = Connect.objects.filter(lawyer=Lawyer.objects.get(user=request.user)).count()
			return render(request, 'StakeHolders/dashboard.html', { 'page': page, 'content': content })
	raise Http404()

@login_required
def signout(request):
	logout(request)
	return redirect('/')