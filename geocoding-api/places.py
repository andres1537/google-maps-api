import googlemaps

key = 'YOUR_API_KEY'

language = 'es'

# Google Maps client
gmaps = googlemaps.Client(key=key)

def reverse_geocode(coordinate):
    """Get the formatted address from the coordinate lat/long."""
    data = gmaps.reverse_geocode(coordinate)
    return data[0].get('formatted_address')