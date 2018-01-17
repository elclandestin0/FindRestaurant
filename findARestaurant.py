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


# def user():
#     user_greeting = """Please select the following:
#           1) Find the top 3 articles of all time OR
#           2) Find the top authors of all time OR
#           3) Find the day where more than 1 percent OR
#           of the requests lead to errors OR
#           0) Exit program \n"""
#     user_input = input(user_greeting)
#     if user_input == 1:
#         first_query()
#         user()
#     elif user_input == 2:
#         second_query()
#         user()
#     elif user_input == 3:
#         third_query()
#         user()
#     elif user_input == 0:
#         print "Good-bye.\n"
#         sys.exit()
#     else:
#         print "Invalid input!\n"
#         user()
#
# if __name__ == "__main__":
#     user()

def user():
    mealType=""
    location=""
    user_greeting = '''
    Hello and welcome to the findARestaurant program! This program
    mashes up the Google Maps and Foursquare API. After inputting
    the meal type and location of interest, the program responds back
    with a dictionary of a restaurant name, address and it's id!
    '''
    meal_input = "Input the meal type: "
    location_input = "Input the location: "
    print user_greeting
    mealType = raw_input(meal_input)
    location = raw_input(location_input)
    findARestaurant(mealType, location)

if __name__ == "__main__":
    user()
# findARestaurant("Tea", "Amsterdam")
