import googlemaps
import requests
import base64

MAPS_API_KEY = "AIzaSyCEO1sbtXCXAR9hmBAn4Ynj3FjnGkXcb8E"
PLACES_ENDPOINT = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
PHOTOS_ENDPOINT = "https://maps.googleapis.com/maps/api/place/photo?"
gmaps = googlemaps.Client(key=MAPS_API_KEY)


def get_places(place_query):
    params = {
        "query": place_query,
        "key": MAPS_API_KEY
    }
    response = requests.get(url=PLACES_ENDPOINT, params=params)
    all_place = response.json()['results']
    places_details = []
    for place in all_place:
        name = place.get('name', 'key_not_found')
        address = place.get('formatted_address', 'key_not_found')
        photo = place.get('photos', 'key_not_found')

        if name == 'key_not_found' or address == 'key_not_found' or photo == 'key_not_found':
            continue
        photo_ref = photo[0]['photo_reference']
        params = {
            "photo_reference": photo_ref,
            "maxheight": 1600,
            "maxwidth": 1600,
            "key": MAPS_API_KEY
        }
        photo = requests.get(url=PHOTOS_ENDPOINT, params=params)
        image = base64.b64encode(photo.content).decode("utf-8")
        place_dict = {
            "name": name,
            "address": address,
            "image": image
        }
        places_details.append(place_dict)
    return places_details
