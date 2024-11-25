from django import forms

FAVORITE_CITIES_CHOICES = [
    ('CHICAGO', 'Chicago, IL'),
    ('DALLAS', 'Dallas, TX'),
    ('FAIRBANKS', 'Fairbanks, AK'),
    ('HOUSTON', 'Houston, TX'),
    ('LOS ANGELES', 'Los Angeles, CA'),
    ('MINNEAPOLIS', "Minneapolis, MN"),
    ('NEW YORK CITY', "New York City, NY"),
    ('PHILADELPHIA', 'Philadelphia, PA'),
    ('PHOENIX', 'Phoenix, AZ'),
    ('SAN ANTONIO', "San Antonio, TX"),
    ('SAN DIEGO', "San Diego, CA"), 
    ('SAN FRANCISCO', "San Francisco, CA"),
]

class CitiesForm(forms.Form):
    favorite_city = forms.ChoiceField(choices=FAVORITE_CITIES_CHOICES)