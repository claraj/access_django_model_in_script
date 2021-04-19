# Accessing Django models from a script, e.g. to populate DB

travel_wishlist/random_place_name.py connects to an API, gets a random place and writes it to the app's db.   
This file needs to import the project's settings.py to be able to access the DB and also import the models without error.

You can run this file from the terminal, in the same location as manage.py with `python travel_wishlist/random_place_model.py` 

An alternative is to create a custom management command. https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/