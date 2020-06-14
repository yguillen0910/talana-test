
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.utils import timezone

from products.models import Car  



class CarsAvailableAPI(APIView):

    def get(self, request):
        cars = []
        return Response(cars, status=HTTP_200_OK)

