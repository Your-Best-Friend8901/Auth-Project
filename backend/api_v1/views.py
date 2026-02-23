from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class HealView(APIView):
    def get(self,request):

        data = {'version':'1'}

        return Response(data,status.HTTP_200_OK)