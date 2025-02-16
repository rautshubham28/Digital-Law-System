import cv2

class FaceDetection:
	def __init__(self):
		self.face_cascade = cv2.CascadeClassifier('Applications/face_detection.xml')	# Load Face Model in Cascade Classifier

	def detector(self, image):
		faces = self.face_cascade.detectMultiScale(image, 1.1, 4)		# Detect Faces in image: (data, scaleFactor, minNeighbours)
		return len(faces) == 1

if __name__ == "__main__":
	faceDetector = FaceDetector()
	image = cv2.imread('face.jpg', 0)
	print(faceDetector.detector(image))