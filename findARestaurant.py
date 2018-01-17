from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

# The Foursquare client ID and client secret are intended
# for my use only if you are interested, you can get your
# own API key @https://developer.foursquare.com

foursquare_client_id = "PVYC4HWHSBIQWWKH4TKWR2UXGR5FVWKNIUEVKOKQVGM0BNFM"
foursquare_client_secret = "IOOVRHSXQGICSDPULID0VPN23D35TFASEKBKJWLZKHAGMSYF"


def findARestaurant(mealType, location):
    '''
    The function takes in the returned variables from getGeocodeLocation
    and inputs it into the url variable. It also inputs the client_id,
    client_secret and mealType to successfully query the list of venues,
    serialized into JSON. From there, we want to find the first restaurant
    in the search query. In doing so, we parse the venue_id, restaurant_name,
    and restaurant_address. Next, we plug it into a restaurant dictionary
    and return the results to the user.
    '''
    latitude, longitude = getGeocodeLocation(location)
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret, latitude, longitude, mealType))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    # Retrieve the first restaurant from the search query.
    restaurant = result['response']['venues'][0]
    venue_id = restaurant['id']
    restaurant_name = restaurant['name']
    restaurant_address = restaurant['location']['address']
    restaurant_dict={
        "id": venue_id,
        "name": restaurant_name,
        "address": restaurant_address
    }
    print restaurant_dict

findARestaurant('Burger','Amsterdam')
# findARestaurant("Tea", "Amsterdam")
