#modified to look like https://www.geeksforgeeks.org/how-to-add-url-parameters-to-django-template-url-tag/
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.db.models import Avg, Max, Min
from .models import ImportTemps
from .forms import CitiesForm
from datetime import datetime, date

#path="" on basicsite.urls.py calls avgs.urls.py which calls def index_view which renders
#  index.html for the browser. When the user selects option 1, 2, or 3, it hrefs to one
#  of these 3 functions based on option selected. These in turn get the necessary
#  info and render the appropriate page (display_daily.html, display.html, etc)
def daily(request, id):
    the_day = request.POST.get('the_day', 'Not Provided')
    the_month = request.POST.get('the_month', 'Not Provided')
    location = request.POST.get('favorite_city', 'No City Provided')
    loc = location[:5]
    location=location.title()
    #currentdate = timezone.now() #this will become a param that is passed
    #currentdate = datetime.strptime(date, '%m-%d-%Y')
    #mon_long = currentdate.strftime("%B")
    mon = the_month   #currentdate.month
    lmon = ("0" + mon)[-2:]
    day = the_day     #currentdate.day
    lday = ("0" + day)[-2:]
    yr = "2024"       #currentdate.year
    mon_long = date.fromisoformat(yr+lmon+lday).strftime("%B")
    today_avg = (ImportTemps.objects.filter(location__startswith=loc)
                  .filter(tdate__month=mon)
                  .filter(tdate__day=day)
                  .aggregate(Avg("tmax"), 
                             Avg('tmin'), 
                             Max('tmax'), 
                             Min('tmax'), 
                             Min  ('tmin'), 
                             Max('tmin')))
    decade1910 = calc_decade(loc, '191', mon, day)
    decade1920 = calc_decade(loc, '192', mon, day)
    decade1930 = calc_decade(loc, '193', mon, day)
    decade1940 = calc_decade(loc, '194', mon, day)
    decade1950 = calc_decade(loc, '195', mon, day)
    decade1960 = calc_decade(loc, '196', mon, day)
    decade1970 = calc_decade(loc, '197', mon, day)
    decade1980 = calc_decade(loc, '198', mon, day)
    decade1990 = calc_decade(loc, '199', mon, day)
    decade2000 = calc_decade(loc, '200', mon, day)
    decade2010 = calc_decade(loc, '201', mon, day)
    decade2020 = calc_decade(loc, '202', mon, day)
    hottest10 = calc_hottest10(loc)
    coldest10 = calc_coldest10(loc)
    context = {'id': id, 
               'location': location,
               'loc':loc,
               'mon_long': mon_long,
               'mon':mon, 
               'day':day, 
               'yr': yr,
               'today_avg': today_avg,
               'decade1910': decade1910,
               'decade1920': decade1920,
               'decade1930': decade1930,
               'decade1940': decade1940,
               'decade1950': decade1950,
               'decade1960': decade1960,
               'decade1970': decade1970,
               'decade1980': decade1980,
               'decade1990': decade1990,
               'decade2000': decade2000,
               'decade2010': decade2010,
               'decade2020': decade2020,
               'hottest10': hottest10,
               'coldest10': coldest10,
               #'date': date,
               'type':'Daily Avgs'} #Type is shown in tab title
    return render(request, "avgs/display_daily.html", context)

def calc_decade(loc, dec, mon, day):
     return (ImportTemps.objects.filter(location__startswith=loc)
                  .filter(tdate__year__contains=dec)
                  .filter(tdate__month=mon)
                  .filter(tdate__day=day)
                  .aggregate(Avg("tmax"), 
                             Avg('tmin'), 
                             Max('tmax'), 
                             Min('tmax'), 
                             Min('tmin'), 
                             Max('tmin')))

def calc_hottest10(loc):
     return ImportTemps.objects.filter(location__startswith=loc).order_by('-tmax')[:10]

def calc_coldest10(loc):
    return ImportTemps.objects.filter(location__startswith=loc).filter(tmin__gt=-300).order_by('tmin')[:10]

def summary_view(request, id):
    month = request.GET.get('month', 'Not provided')
    context = {'id': id, 'date': month, 'type': 'Select Date'}
    return render(request, 'avgs/display.html', context)

def report_view(request, id):
    year = request.GET.get('year', 'Not provided')
    context = {'id': id, 'date': year, 'type': 'Overall Avgs'}
    return render(request, 'avgs/display.html', context)

# This func is called when main site visited with path="" and displays main index page
def index_view(request):
    form = CitiesForm()
    return render(request, 'avgs/index.html', {'form':form})