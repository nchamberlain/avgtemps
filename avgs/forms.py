from django import forms

FAVORITE_CITIES_CHOICES = [
    ('CHICA', 'Chicago, IL'),
    ('DALLA', 'Dallas, TX'),
    ('FAIRB', 'Fairbanks, AK'),
    ('HOUST', 'Houston, TX'),
    ('LOS A', 'Los Angeles, CA'),
    ('MINNE', "Minneapolis, MN"),
    ('NEW Y', "New York City, NY"),
    ('PHILA', 'Philadelphia, PA'),
    ('PHOEN', 'Phoenix, AZ'),
    ('SAN A', "San Antonio, TX"),
    ('SAN D', "San Diego, CA"), 
    ('SAN F', "San Francisco, CA")
]

class CitiesForm(forms.Form):
    favorite_city = forms.ChoiceField(choices=FAVORITE_CITIES_CHOICES)