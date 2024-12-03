from django import forms
from datetime import datetime
from django.forms.widgets import NumberInput

FAVORITE_CITIES_CHOICES = [
    ('BILLINGS', 'Billings, MT'),
    ('BISMARCK', 'Bismarck, ND'),
    ('CHICAGO', 'Chicago, IL'),
    ('COLUMBUS', 'Columbus, OH'),
    ('DALLAS', 'Dallas, TX'),
    ('FAIRBANKS', 'Fairbanks, AK'),
    ('HOUSTON', 'Houston, TX'),
    ('INDIANAPOLIS', 'Indianapolis, IN'),
    ('JACKSONVILLE','Jacksonville, FL'),
    ('LOS ANGELES', 'Los Angeles, CA'),
    ('MINNEAPOLIS', "Minneapolis, MN"),
    ('NASHVILLE', 'Nashville, TN'),
    ('NEW YORK CITY', "New York City, NY"),
    ('OKLAHOMA CITY', 'Oklahoma City, OK'),
    ('PHILADELPHIA', 'Philadelphia, PA'),
    ('PHOENIX', 'Phoenix, AZ'),
    ('SAN ANTONIO', "San Antonio, TX"),
    ('SAN DIEGO', "San Diego, CA"), 
    ('SAN FRANCISCO', "San Francisco, CA"),
    ('SEATTLE', 'Seattle, WA'),
    ('SPOKANE', 'Spokane, WA'),
]

THE_MONTH_NBR = [
    ("1","January"),
    ("2", "February"),
    ("3", "March"),
    ("4", "April"),
    ("5", "May"),
    ("6", "June"),
    ("7", "July"),
    ("8", "August"),
    ("9", "September"),
    ("10", "October"),
    ("11", "November"),
    ("12", "December"),
]

THE_DAY_NUMBER = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ("13", "13"),
    ("14", "14"),
    ("15", "15"),
    ("16", "16"),
    ("17", "17"),
    ("18", "18"),
    ("19", "19"),
    ("20", "20"),
    ("21", "21"),
    ("22", "22"),
    ("23", "23"),
    ("24", "24"),
    ("25", "25"),
    ("26", "26"),
    ("27", "27"),
    ("28", "28"),
    ("29", "29"),
    ("30", "30"),
    ("31", "31"),
]

class CitiesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CitiesForm, self).__init__(*args, **kwargs)
        self.fields['the_month'].initial = str(datetime.now().month)
        self.fields['the_day'].initial= str(datetime.now().day)
        
    favorite_city = forms.ChoiceField(choices=FAVORITE_CITIES_CHOICES, initial="LOS ANGELES")
    #date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    the_month = forms.ChoiceField(choices = THE_MONTH_NBR)
    the_day = forms.ChoiceField(choices = THE_DAY_NUMBER)