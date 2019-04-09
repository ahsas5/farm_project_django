import datetime
from datetime import timedelta
from django.http import HttpResponse
from .models import Farm, Farmer, Schedule_detail
from django.db.models import Sum


def farmers_grow_crop(request):
    data = Farm.objects.all().values_list('farmer', flat=True).distinct()
    return HttpResponse("crops query processing done")


def schedules_due_today_tom(request):
    today = datetime.date.today()
    tomorrow = datetime.date.today() + timedelta(1)
    schedules_due = Schedule_detail.objects.filter(due_date__in=[today, tomorrow])
    return HttpResponse("schedules query processing done")


def bill_for_fertiliser(request, pk=1):
    farmer_id = pk  # assuming pk from url or in request_obj
    bill_per_farmer = Schedule_detail.objects.filter(farm__farmer=farmer_id).aggregate(Sum('price'))
    return HttpResponse(" bill query processing done")
