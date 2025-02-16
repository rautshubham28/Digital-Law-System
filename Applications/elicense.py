from PIL import Image, ImageDraw, ImageFont

class ELicense:
	def __init__(self):
		self.img = Image.new('1', (800, 1000), 1)
		self.font_title = ImageFont.truetype('Applications/times.ttf', 40)
		self.font_body = ImageFont.truetype('Applications/times.ttf', 25)
		self.draw = ImageDraw.Draw(self.img)

	def generate(self, elicense_type, name=None, age=None, gender=None, address=None, annual_income=None,
	vehicle=None, duration=None, reason=None, source=None, destination=None, members=None):
		if elicense_type == 'ration':
			self.draw.text((800/2, 100), "E-RATION CARD", font=self.font_title, fill=0, anchor="mm")
			self.draw.text((100, 250), 'Head of Family: ', font=self.font_body, fill=0)
			self.draw.text((300, 250), name, font=self.font_body, fill=0)
			self.draw.text((100, 300), 'Age: ', font=self.font_body, fill=0)
			self.draw.text((300, 300), age, font=self.font_body, fill=0)
			self.draw.text((100, 350), 'Gender: ', font=self.font_body, fill=0)
			self.draw.text((300, 350), gender, font=self.font_body, fill=0)
			self.draw.text((100, 400), 'Address: ', font=self.font_body, fill=0)
			self.draw.text((300, 400), address, font=self.font_body, fill=0)
			self.draw.text((100, 450), 'Annual Income: ', font=self.font_body, fill=0)
			self.draw.text((300, 450), annual_income, font=self.font_body, fill=0)
			if members:
				self.draw.text((100, 550), 'Family Members: ', font=self.font_body, fill=0)
				box_y, text_y = 600, 625
				for member in members:
					self.draw.rectangle((100, box_y, 700, box_y+50), outline=0)
					self.draw.text((800/2, text_y), member['member'], font=self.font_body, fill=0, anchor="mm")
					box_y += 50
					text_y += 50
		elif elicense_type == 'epass':
			self.draw.text((800/2, 100), "COVID E-PASS", font=self.font_title, fill=0, anchor="mm")
			self.draw.text((100, 250), 'Applicant Name: ', font=self.font_body, fill=0)
			self.draw.text((300, 250), name, font=self.font_body, fill=0)
			self.draw.text((100, 300), 'Vehicle Number: ', font=self.font_body, fill=0)
			self.draw.text((300, 300), vehicle, font=self.font_body, fill=0)
			self.draw.text((100, 350), 'Pass Validity: ', font=self.font_body, fill=0)
			self.draw.text((300, 350), duration + ' days', font=self.font_body, fill=0)
			self.draw.text((100, 400), 'Reason for Travel: ', font=self.font_body, fill=0)
			self.draw.text((300, 400), reason, font=self.font_body, fill=0)
			self.draw.text((100, 450), 'Route Origin: ', font=self.font_body, fill=0)
			self.draw.text((300, 450), source, font=self.font_body, fill=0)
			self.draw.text((100, 500), 'Route Destination: ', font=self.font_body, fill=0)
			self.draw.text((300, 500), destination, font=self.font_body, fill=0)
			if members:
				self.draw.text((100, 600), 'Travelling Members: ', font=self.font_body, fill=0)
				box_y, text_y = 650, 675
				for member in members:
					self.draw.rectangle((100, box_y, 700, box_y+50), outline=0)
					self.draw.text((800/2, text_y), member['member'], font=self.font_body, fill=0, anchor="mm")
					box_y += 50
					text_y += 50
		elif elicense_type == 'pharmacy':
			self.draw.text((800/2, 100), "PHARMACY LICENSE", font=self.font_title, fill=0, anchor="mm")
			self.draw.text((100, 250), 'Owner Name: ', font=self.font_body, fill=0)
			self.draw.text((300, 250), name, font=self.font_body, fill=0)
			self.draw.text((100, 300), 'Age: ', font=self.font_body, fill=0)
			self.draw.text((300, 300), age, font=self.font_body, fill=0)
			self.draw.text((100, 350), 'Gender: ', font=self.font_body, fill=0)
			self.draw.text((300, 350), gender, font=self.font_body, fill=0)
			self.draw.text((100, 400), 'Address of Pharmacy: ', font=self.font_body, fill=0)
			self.draw.text((300, 400), address, font=self.font_body, fill=0)
			self.draw.text((100, 450), 'License Type: ', font=self.font_body, fill=0)
			self.draw.text((300, 450), reason, font=self.font_body, fill=0)
		elif elicense_type == 'travel':
			self.draw.text((800/2, 100), "TRAVEL AGENCY LICENSE", font=self.font_title, fill=0, anchor="mm")
			self.draw.text((100, 250), 'Owner Name: ', font=self.font_body, fill=0)
			self.draw.text((300, 250), name, font=self.font_body, fill=0)
			self.draw.text((100, 300), 'Vehicle Number: ', font=self.font_body, fill=0)
			self.draw.text((300, 300), vehicle, font=self.font_body, fill=0)
			self.draw.text((100, 350), 'Address of Agency: ', font=self.font_body, fill=0)
			self.draw.text((300, 350), address, font=self.font_body, fill=0)
			self.draw.text((100, 400), 'Route Origin: ', font=self.font_body, fill=0)
			self.draw.text((300, 400), source, font=self.font_body, fill=0)
			self.draw.text((100, 450), 'Route Destination: ', font=self.font_body, fill=0)
			self.draw.text((300, 450), destination, font=self.font_body, fill=0)
		elif elicense_type == 'hotel':
			self.draw.text((800/2, 100), "HOTEL LICENSE", font=self.font_title, fill=0, anchor="mm")
			self.draw.text((100, 250), 'Owner Name: ', font=self.font_body, fill=0)
			self.draw.text((300, 250), name, font=self.font_body, fill=0)
			self.draw.text((100, 300), 'Age: ', font=self.font_body, fill=0)
			self.draw.text((300, 300), age, font=self.font_body, fill=0)
			self.draw.text((100, 350), 'Gender: ', font=self.font_body, fill=0)
			self.draw.text((300, 350), gender, font=self.font_body, fill=0)
			self.draw.text((100, 400), 'Address of ' + ('Hotel' if reason == 'Hotel' else 'Restaurant') + ': ', font=self.font_body, fill=0)
			self.draw.text((300, 400), address, font=self.font_body, fill=0)
			self.draw.text((100, 450), 'License Type: ', font=self.font_body, fill=0)
			self.draw.text((300, 450), reason, font=self.font_body, fill=0)
		elif elicense_type == 'rally':
			self.draw.text((800/2, 100), "RALLY LICENSE", font=self.font_title, fill=0, anchor="mm")
			self.draw.text((100, 250), 'Applicant Name: ', font=self.font_body, fill=0)
			self.draw.text((300, 250), name, font=self.font_body, fill=0)
			self.draw.text((100, 300), 'Rally Duration: ', font=self.font_body, fill=0)
			self.draw.text((300, 300), duration + ' hours', font=self.font_body, fill=0)
			self.draw.text((100, 350), 'Reason for Rally: ', font=self.font_body, fill=0)
			self.draw.text((300, 350), reason, font=self.font_body, fill=0)
			self.draw.text((100, 400), 'Route Origin: ', font=self.font_body, fill=0)
			self.draw.text((300, 400), source, font=self.font_body, fill=0)
			self.draw.text((100, 450), 'Route Destination: ', font=self.font_body, fill=0)
			self.draw.text((300, 450), destination, font=self.font_body, fill=0)
			if members:
				self.draw.text((100, 550), 'Rally Members: ', font=self.font_body, fill=0)
				box_y, text_y = 600, 625
				for member in members:
					self.draw.rectangle((100, box_y, 700, box_y+50), outline=0)
					self.draw.text((800/2, text_y), member['member'], font=self.font_body, fill=0, anchor="mm")
					box_y += 50
					text_y += 50
		return self.img

if __name__ == "__main__":
	elicense = ELicense()
	elicense.generate(elicense_type='ration', name='My Lawyer', age='22', gender='Male', address='Pune', annual_income='600000', members=['East', 'West', 'North', 'South']).show()
