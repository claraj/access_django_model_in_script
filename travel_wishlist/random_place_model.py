import os
import django
import sys
import requests 

# include this file location on the path 
sys.path.append(os.getcwd())   
# explain where the settings are - these include where the db is 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wishlist.settings')
django.setup() 

# now this import works 
from travel_wishlist.models import Place 


# http://names.drycodes.com/ Randomly generated weird place names API
random_place_name_api_url = 'http://names.drycodes.com/1?separator=space'

random_place_name_list = requests.get(random_place_name_api_url).json()
random_place_name = random_place_name_list[0]

place = Place(name=random_place_name)
place.save()

print('created new place called', random_place_name)