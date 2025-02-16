import cv2
import numpy as np

MIN_MATCH_COUNT_goi = 75
MIN_MATCH_COUNT_msmdl = 75
MIN_MATCH_COUNT_emblem = 25				# reducable to 20
MIN_MATCH_COUNT_itd = 50
MIN_MATCH_COUNT_motto = 50
MIN_MATCH_COUNT_mmvd = 50
MIN_MATCH_COUNT_logo = 20

class FeatureMatcher:
	def __init__(self):
		self.sift = cv2.SIFT_create()											# Initialize SIFT object
		FLANN_INDEX_KDTREE = 0
		index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)			# IndexParams for selecting algo (currently for SIFT)
		search_params = dict(checks = 50)										# SearchParams No. or times tree traverse recursively
		self.flann = cv2.FlannBasedMatcher(index_params, search_params)			# Create FLANN Matcher with above parameters
		goi_aadhar = cv2.imread('Applications/samples/aadhar/goi.jpg',0)
		emblem_aadhar = cv2.imread('Applications/samples/aadhar/emblem.jpg',0)
		motto_aadhar = cv2.imread('Applications/samples/aadhar/motto.jpg',0)		# Read all notable features in each of the
		goi_pan = cv2.imread('Applications/samples/pan/goi.jpg',0)					# documents - Aadhar, Pan, License, Voter ID
		emblem_pan = cv2.imread('Applications/samples/pan/emblem.jpg',0)
		itd_pan = cv2.imread('Applications/samples/pan/itd.jpg',0)
		msmdl_license = cv2.imread('Applications/samples/license/msmdl.jpg',0)
		emblem_license = cv2.imread('Applications/samples/license/emblem.jpg',0)
		mmvd_license = cv2.imread('Applications/samples/license/mmvd.jpg',0)
		emblem_voter_id = cv2.imread('Applications/samples/voter_id/emblem.jpg',0)
		logo_voter_id = cv2.imread('Applications/samples/voter_id/logo.jpg',0)
		kp_goi_aadhar, self.des_goi_aadhar = self.sift.detectAndCompute(goi_aadhar,None)
		kp_emblem_aadhar, self.des_emblem_aadhar = self.sift.detectAndCompute(emblem_aadhar,None)
		kp_motto_aadhar, self.des_motto_aadhar = self.sift.detectAndCompute(motto_aadhar,None)
		kp_goi_pan, self.des_goi_pan = self.sift.detectAndCompute(goi_pan,None)				# Find the keypoints and descriptors
		kp_emblem_pan, self.des_emblem_pan = self.sift.detectAndCompute(emblem_pan,None)	# of notable features using SIFT
		kp_itd_pan, self.des_itd_pan = self.sift.detectAndCompute(itd_pan,None)
		kp_msmdl_license, self.des_msmdl_license = self.sift.detectAndCompute(msmdl_license,None)
		kp_emblem_license, self.des_emblem_license = self.sift.detectAndCompute(emblem_license,None)
		kp_mmvd_license, self.des_mmvd_license = self.sift.detectAndCompute(mmvd_license,None)
		kp_emblem_voter_id, self.des_emblem_voter_id = self.sift.detectAndCompute(emblem_voter_id,None)
		kp_logo_voter_id, self.des_logo_voter_id = self.sift.detectAndCompute(logo_voter_id,None)

	def verifier(self, image, id_type):
		kp_image, des_image = self.sift.detectAndCompute(image,None)	# Find the keypoints and descriptors of query image using SIFT
		if id_type == 'aadhar':
			matches_goi = self.flann.knnMatch(des_image,self.des_goi_aadhar,k=2)			# Check for matches of each feature
			matches_emblem = self.flann.knnMatch(des_image,self.des_emblem_aadhar,k=2)		# using FLANN matcher
			matches_motto = self.flann.knnMatch(des_image,self.des_motto_aadhar,k=2)
			# store all the good matches as per Lowe's ratio test.
			count_goi = 0
			for m,n in matches_goi:													# First, we match the keypoints in Query Image
				if m.distance < 0.7*n.distance:										# with two keypoints in Sample Image. Considering
					count_goi += 1													# the assumption that a keypoint in query image
			count_emblem = 0														# can't have more than one equivalent in sample
			for m,n in matches_emblem:												# image, we deduce that those two matches can't
				if m.distance < 0.7*n.distance:										# both be right: at least one of them is wrong. 
					count_emblem += 1												# Lowe's reasoning states that one of them is a
			count_motto = 0															# "good" match and other is noise. If the "good"
			for m,n in matches_motto:												# match can't be distinguished from noise, then
				if m.distance < 0.7*n.distance:										# the "good" match should be rejected because
					count_motto += 1												# it does not bring any useful information.
			if count_goi < MIN_MATCH_COUNT_goi or count_emblem < MIN_MATCH_COUNT_emblem or count_motto < MIN_MATCH_COUNT_motto:
				return False														# If the count of matches for each sample are above
			return True																# a threshold, accept the document else reject it.
		elif id_type == 'pan':
			matches_goi = self.flann.knnMatch(des_image,self.des_goi_pan,k=2)
			matches_emblem = self.flann.knnMatch(des_image,self.des_emblem_pan,k=2)
			matches_itd = self.flann.knnMatch(des_image,self.des_itd_pan,k=2)
			# store all the good matches as per Lowe's ratio test.
			count_goi = 0
			for m,n in matches_goi:
				if m.distance < 0.7*n.distance:
					count_goi += 1
			count_emblem = 0
			for m,n in matches_emblem:
				if m.distance < 0.7*n.distance:
					count_emblem += 1
			count_itd = 0
			for m,n in matches_itd:
				if m.distance < 0.7*n.distance:
					count_itd += 1
			if count_goi < MIN_MATCH_COUNT_goi or count_emblem < MIN_MATCH_COUNT_emblem or count_itd < MIN_MATCH_COUNT_itd:
				return False
			return True
		elif id_type == 'driving_license':
			matches_msmdl = self.flann.knnMatch(des_image,self.des_msmdl_license,k=2)
			matches_emblem = self.flann.knnMatch(des_image,self.des_emblem_license,k=2)
			matches_mmvd = self.flann.knnMatch(des_image,self.des_mmvd_license,k=2)
			# store all the good matches as per Lowe's ratio test.
			count_msmdl = 0
			for m,n in matches_msmdl:
				if m.distance < 0.7*n.distance:
					count_msmdl += 1
			count_emblem = 0
			for m,n in matches_emblem:
				if m.distance < 0.7*n.distance:
					count_emblem += 1
			count_mmvd = 0
			for m,n in matches_mmvd:
				if m.distance < 0.7*n.distance:
					count_mmvd += 1
			if count_msmdl <=MIN_MATCH_COUNT_msmdl or count_emblem < MIN_MATCH_COUNT_emblem or count_mmvd < MIN_MATCH_COUNT_mmvd:
				return False
			return True
		elif id_type == 'voter_id':
			matches_emblem = self.flann.knnMatch(des_image,self.des_emblem_voter_id,k=2)
			matches_logo = self.flann.knnMatch(des_image,self.des_logo_voter_id,k=2)
			print(matches_logo)
			# store all the good matches as per Lowe's ratio test.
			count_emblem = 0
			for m,n in matches_emblem:
				if m.distance < 0.7*n.distance:
					count_emblem += 1
			count_logo = 0
			for m,n in matches_logo:
				if m.distance < 0.7*n.distance:
					count_logo += 1
			if count_emblem < MIN_MATCH_COUNT_emblem or count_logo < MIN_MATCH_COUNT_logo:
				return False
			return True

if __name__ == "__main__":
	featureMatcher = FeatureMatcher()
	image = cv2.imread('example/voter_id.jpg',0)
	print(featureMatcher.verifier(image, 'voter_id'))