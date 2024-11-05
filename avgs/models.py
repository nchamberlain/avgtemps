from django.db import models

# Holds data imported from Weather Source for ONE location (city data station)
# which has the temps for every day of every year between 1910's to 2020's
class ImportTemps(models.Model):
    station = models.CharField(max_length=32)
    location = models.CharField(max_length=64)
    tdate = models.DateField()
    tmax = models.IntegerField(null=True)
    tmin = models.IntegerField(null=True)
    tobs = models.IntegerField(null=True)

    def __str__(self):
        return self.location + " " + str(self.tdate) + " " + str(self.tmax) + " " + str(self.tmin)

class Station(models.Model):
    station = models.CharField(max_length=32)
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.description

class AllTemps(models.Model):
    tdate = models.DateField()
    tmax = models.IntegerField(null=True)
    tmin = models.IntegerField(null=True)
    location = models.ForeignKey(Station, 
                                 to_field="id",
                                 on_delete=models.CASCADE,
                                 null=True)
    
    def __str__(self):
        return self.tdate + ": " + str(self.location) + " High: " + str(self.tmax) + " Low: " + str(self.tmin)