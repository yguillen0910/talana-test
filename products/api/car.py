
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.utils import timezone
from django.db.models import Q
from products.models import Car  
from products.models import Reservation



class CarsAvailableAPI(APIView):

    def get(self, request):
        dates = []
        dates.append(request.GET.get('start', ''))
        dates.append(request.GET.get('end', ''))
        dates.sort()
        cars_reserved = Reservation.objects.filter(
            Q(start__range=[dates[0], dates[1]]) | 
                Q(end__range=[dates[0], dates[1]])
        ).values_list('car__id', flat=True)
        
        cars = (Car.objects
            .exclude(id__in=cars_reserved)
            .values(
            'id',
            'name',
            'description',
            'patent',
            'size',
            'number_of_doors',
            'diesel',
            'model__name',
            'model__brand__name'))

        return Response(cars, status=HTTP_200_OK)