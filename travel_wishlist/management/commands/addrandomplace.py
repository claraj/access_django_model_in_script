from django.core.management.base import BaseCommand
from travel_wishlist.models import Place 
import requests

class Command(BaseCommand):
    
    def handle(self, *args, **options):

        # http://names.drycodes.com/ Randomly generated weird place names API
        random_place_name_api_url = 'http://names.drycodes.com/1?separator=space'

        random_place_name_list = requests.get(random_place_name_api_url).json()
        random_place_name = random_place_name_list[0]

        place = Place(name=random_place_name)
        place.save()

        self.stdout.write(self.style.SUCCESS(f'Added place name {random_place_name}'))