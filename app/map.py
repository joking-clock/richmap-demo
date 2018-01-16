import googlemaps

class MapService:
	'''def __init__(self):
		self.gmaps = googlemaps.Client(key='AIzaSyCts7em4L-ni5Lrc1goEXae-uqyVwtIcxI')'''

	def geocode(self, address):
		gmaps = googlemaps.Client(key='AIzaSyCts7em4L-ni5Lrc1goEXae-uqyVwtIcxI')
		geocode_result = gmaps.geocode(address)
		return geocode_result[0]['geometry']['location']

	'''def degeocode(self, coordinates):
		reverse_geocode_result = gmaps.reverse_geocode((coordinates[], coordinates[]))
		return reverse_geocode_result'''