import httplib2
import json
def getGeocodeLocation(inputString):
    '''
    This is a custom-made module named geocode. We import getGeocodeLocation
    from geocode in findARestaurant.py. Once we pass in an input string, the
    function replaces the spaces (" ") with a plus sign ("+"). This is a
    crucial format for getting a proper HTTP 200 GET request. Once we
    receive a proper get-request, we load the result in json, and parse
    two parameters from the Google Maps API, which are the longitude
    and latitude of the city in question. We use these parsed variables
    to input into our Foursquare API GET request, found in findARestaurant.py
    '''
    # the Google API key is intended for my use only. If you are interested
    # in working with this project, you can request your own API key from
    # Google on developers.google.com. Thank you for understanding
    google_api_key = "AIzaSyA-pnTIuJqwtfsInE9n1slQictD0FdJjNI"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (locationString, google_api_key))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)
