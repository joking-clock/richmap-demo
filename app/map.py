import googlemaps

class MapService:
	'''def __init__(self):
		self.gmaps = googlemaps.Client(key='api key')'''

	def geocode(self, address):
		gmaps = googlemaps.Client(key='api key')	# input Google Map API key
		geocode_result = gmaps.geocode(address)
		return geocode_result[0]['geometry']['location']

	'''def degeocode(self, coordinates):
		reverse_geocode_result = gmaps.reverse_geocode((coordinates[], coordinates[]))
		return reverse_geocode_result'''
