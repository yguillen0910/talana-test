
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.utils import timezone
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
import uuid



class Login(APIView):

    def get(self, request):
        password = request.GET.get('password', None)
        username = request.GET.get('username', None)

        if not password or not username:
            return Response({'login': False}, status=HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        print(dir(user))
        if not user:
            return Response({'login': False}, status=HTTP_404_NOT_FOUND)
        return Response({'token': uuid.uuid4().hex}, status=HTTP_200_OK)
