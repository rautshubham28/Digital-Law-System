from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Application
from .feature_matcher import FeatureMatcher
from .face_detection import FaceDetection
from .elicense import ELicense
import cv2
import numpy as np
from base64 import b64encode
from io import BytesIO

featureMatcher = FeatureMatcher()
faceDetection = FaceDetection()
elicense = ELicense()

# Create your views here.
def index(request):
	return render(request, 'Applications/index.html')

@login_required
def form(request, form):
	if form in ['ration', 'epass', 'pharmacy', 'hotel', 'travel', 'rally']:
		if request.method == 'POST':
			# pass
			errors = []
			name = request.POST['name']
			mobile = request.POST['mobile']
			email = request.POST['email']
			address = request.POST['address'] if 'address' in request.POST else None						# Accept form inputs into
			age = request.POST['age'] if 'age' in request.POST else None									# respective variables, with
			gender = request.POST['gender'] if 'gender' in request.POST else None							# the optional variables
			annual_income = request.POST['annual_income'] if 'annual_income' in request.POST else None		# being set to 'None' if they
			count = int(request.POST['count']) if 'count' in request.POST else None							# don't exist in current form
			source = request.POST['source'] if 'source' in request.POST else None
			destination = request.POST['destination'] if 'destination' in request.POST else None
			reason = request.POST['reason'] if 'reason' in request.POST else None
			vehicle = request.POST['vehicle'] if 'vehicle' in request.POST else None
			duration = request.POST['duration'] if 'duration' in request.POST else None
			members = [ { 'member': request.POST['member'+str(i)]} for i in range(count) ] if count else []
			photo = request.FILES['photo'].read()															# Read the submitted documents
			aadhar = request.FILES['aadhar'].read()															# from the form inputs, to
			pan = request.FILES['pan'].read()																# verify them before accepting
			driving_license = request.FILES['driving_license'].read()										# and storing the form in
			voter_id = request.FILES['voter_id'].read()														# database for approval.
			image_photo =  cv2.imdecode(np.fromstring(photo, np.uint8), cv2.IMREAD_UNCHANGED)
			image_aadhar =  cv2.imdecode(np.fromstring(aadhar, np.uint8), cv2.IMREAD_UNCHANGED)				# Documents conversion to
			image_pan = cv2.imdecode(np.fromstring(pan, np.uint8), cv2.IMREAD_UNCHANGED)					# relevant datatype
			image_driving_license = cv2.imdecode(np.fromstring(driving_license, np.uint8), cv2.IMREAD_UNCHANGED)
			image_voter_id = cv2.imdecode(np.fromstring(voter_id, np.uint8), cv2.IMREAD_UNCHANGED)
			image_elicense = elicense.generate(elicense_type=form, name=name, age=age, gender=gender, address=address, duration=duration,
			annual_income=annual_income, source=source, destination=destination, reason=reason, vehicle=vehicle,members=members)
			image_buffer = BytesIO()																# Generate license to store in database
			image_elicense.save(image_buffer, format='JPEG')										# Will only be available after approval
			if not faceDetection.detector(image_photo):
				errors.append('photo')																# Verify Applicant's photo, Aadhar
			if not featureMatcher.verifier(image_aadhar, 'aadhar'):									# Card, Pan Card, Driving License,
				errors.append('aadhar')																# Voter ID Card by checking logos &
			if not featureMatcher.verifier(image_pan, 'pan'):										# emblems present on these documents
				errors.append('pan')																# and add document name to 'errors'
			if not featureMatcher.verifier(image_driving_license, 'driving_license'):				# list if document doesn't satisfy
				errors.append('driving_license')													# the conditions. 'errors' list will
			if not featureMatcher.verifier(image_voter_id, 'voter_id'):								# be used to notify the user.
				errors.append('voter_id')
			if len(errors) == 0:
				application = Application.objects.create(name=name, mobile=mobile, address=address, email=email, age=age, gender=gender,
					annual_income=annual_income, source=source, destination=destination, reason=reason, vehicle=vehicle, duration=duration,
					members=members, user=request.user, application_type=form,						# If no errors found, add application
					photo=b64encode(photo).decode('utf8'),											# to database, which will be Approved/
					aadhar=b64encode(aadhar).decode('utf8'),										# Rejected by admin after review.
					driving_license=b64encode(driving_license).decode('utf8'),						# User can check for approval status
					pan=b64encode(pan).decode('utf8'),												# on dashboard. Application can be
					voter_id=b64encode(voter_id).decode('utf8'),									# Deleted before Approval, and the
					elicense=b64encode(image_buffer.getvalue()).decode('utf8')						# generated E-license can be downloaded
				)																					# after Approval from Dashboard itself
			return render(request, 'Applications/form.html', { 'form': form, 'errors': errors })
		else:
			return render(request, 'Applications/form.html', { 'form': form, 'errors': None })
	raise Http404()
