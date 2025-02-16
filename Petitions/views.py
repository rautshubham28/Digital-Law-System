from django.shortcuts import render
from django.http import Http404
from .models import Petition
import cv2
import numpy as np
from base64 import b64encode
import datetime
from Applications.feature_matcher import FeatureMatcher
from Applications.face_detection import FaceDetection

featureMatcher = FeatureMatcher()
faceDetection = FaceDetection()

# Create your views here.
def index(request):
	return render(request, 'Petitions/index.html')

def form(request, court):
	if court in ['district', 'high', 'supreme']:
		if request.method == 'POST':
			errors = []
			title = request.POST['title']
			state = request.POST['state'] if 'state' in request.POST else None
			district = request.POST['district'] if 'district' in request.POST else None
			description = request.POST['description']
			petitioner_count = int(request.POST['petitioner_count']) 
			complainee_count = int(request.POST['complainee_count']) 
			petitioners = [ { 'petitioner': request.POST['petitioner'+str(i)]} for i in range(petitioner_count) ]
			complainees = [ { 'complainee': request.POST['complainee'+str(i)]} for i in range(complainee_count) ]
			hearing = datetime.date.today() + datetime.timedelta(7)
			photo = request.FILES['photo'].read()													# Read the submitted documents
			aadhar = request.FILES['aadhar'].read()													# to verify them before accepting
			pan = request.FILES['pan'].read()
			image_photo =  cv2.imdecode(np.fromstring(photo, np.uint8), cv2.IMREAD_UNCHANGED)		# Documents conversion to
			image_aadhar =  cv2.imdecode(np.fromstring(aadhar, np.uint8), cv2.IMREAD_UNCHANGED)		# relevant datatype.
			image_pan = cv2.imdecode(np.fromstring(pan, np.uint8), cv2.IMREAD_UNCHANGED)
			if not faceDetection.detector(image_photo):												# Verify Applicant's photo, Aadhar
				errors.append('photo')																# Card, Pan Card by checking logos
			if not featureMatcher.verifier(image_aadhar, 'aadhar'):									# & emblems present on these
				errors.append('aadhar')																# documents and add document name
			if not featureMatcher.verifier(image_pan, 'pan'):										# to 'errors' list if issues found
				errors.append('pan')																# and inform the user using same.
			if len(errors) == 0:
				petition = Petition.objects.create(title=title, state=state, district=district, description=description, result=None,
					user=request.user, hearing=hearing, court=court, petitioners=petitioners, complainees=complainees,
					photo=b64encode(photo).decode('utf8'),											# Add petition to database if no
					aadhar=b64encode(aadhar).decode('utf8'),										# errors present. inform the user
					pan=b64encode(pan).decode('utf8'),												# about next hearing date.
				)
			return render(request, 'Petitions/form.html', { 'court': court, 'errors': errors, 'hearing': hearing })
		else:
			return render(request, 'Petitions/form.html', { 'court': court, 'errors': None, 'hearing': None })
	raise Http404()