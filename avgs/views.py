#modified to look like https://www.geeksforgeeks.org/how-to-add-url-parameters-to-django-template-url-tag/
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.db.models import Avg, Max, Min
from .models import ImportTemps

#path="" on basicsite.urls.py calls avgs.urls.py which calls index_views.html to be
#  returned to the browser. When the user selects option 1, 2, or 3, it hrefs to one
#  of these 3 functions based on option selected. These in turn get the necessary
#  info and render the display.html with this info but could just as easily call
#  different pages to display the info
def daily(request, id):
    date = request.GET.get('date', 'Not Provided')
    loc = "LOS"  # this will become a param that is passed
    currentdate = timezone.now() #this will become a param that is passed
    mon = currentdate.month
    day = currentdate.day
    yr = currentdate.year
    today_avg = (ImportTemps.objects.filter(location__startswith=loc)
                  .filter(tdate__month=mon)
                  .filter(tdate__day=day)
                  .aggregate(Avg("tmax"), 
                             Avg('tmin'), 
                             Max('tmax'), 
                             Min('tmax'), 
                             Min('tmin'), 
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
    context = {'id': id, 
               'loc':loc,
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

def summary_view(request, id):
    month = request.GET.get('month', 'Not provided')
    context = {'id': id, 'date': month, 'type': 'Select Date'}
    return render(request, 'avgs/display.html', context)

def report_view(request, id):
    year = request.GET.get('year', 'Not provided')
    context = {'id': id, 'date': year, 'type': 'Overall Avgs'}
    return render(request, 'avgs/display.html', context)

def index_view(request):
  	return render(request, 'avgs/index.html')