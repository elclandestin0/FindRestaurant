from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "PVYC4HWHSBIQWWKH4TKWR2UXGR5FVWKNIUEVKOKQVGM0BNFM"
foursquare_client_secret = "IOOVRHSXQGICSDPULID0VPN23D35TFASEKBKJWLZKHAGMSYF"


def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url
    latitude, longitude = getGeocodeLocation(location)
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret, latitude, longitude, mealType))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
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

    #print restaurant_name
    #print restaurant_address
    # for row in result:
    #     print row
    # # print result
    # return result
    # url_venue = ('https://api.foursquare.com/v2/venues/search')
    # return result
    # return restaurant

findARestaurant('Burger','Amsterdam')
# findARestaurant("Tea", "Amsterdam")
