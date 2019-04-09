from django.db import models

UNIT_CHOICES = (
    ('ton', 'Ton'),
    ('kg', 'Kilograms'),
    ('g', 'grams'),
    ('L', 'litres'),
    ('mL', 'millitres'),
)


# Create your models here.
class Farmer(models.Model):
    farmer_id = models.IntegerField(primary_key=True, default=1)
    name = models.CharField(blank=False, max_length=255)
    phone_number = models.CharField(blank=False, max_length=15)
    language = models.TextField(blank=False)

    def __str__(self):
        return self.name


class Farm(models.Model):
    area = models.FloatField(blank=False)  # size
    village = models.CharField(blank=False, max_length=255)
    crop_grown = models.CharField(blank=True, max_length=255)
    sowing_date = models.DateTimeField(auto_now_add=False)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return Farm.id


class Schedule_detail(models.Model):
    days_after_sowing = models.IntegerField(blank=False)
    Fertiliser = models.CharField(blank=True, max_length=255)
    quantity = models.IntegerField(blank=False)
    quantity_unit = models.CharField(choices=UNIT_CHOICES, max_length=10)
    price = models.FloatField(blank=False, default=0)
    due_date = models.DateTimeField(auto_now_add=False, null=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return Schedule_detail.id
