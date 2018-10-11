'''
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RTO_Details
from .serializer import RTO_DetailsSerializer

# Create views using APIVIEW.
class RTO_DetailsList(APIView):
	def get(self,request):
		emp=RTO_Details.objects.all()
		serializers_obj=RTO_DetailsSerializer(emp,many=True)
		return Response(serializers_obj.data)
'''

# code for ViewSet

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import RTO_Details
from .serializer import RTO_DetailsSerializer

class RTO_DetailsViewSet(ModelViewSet):
    queryset = RTO_Details.objects.all()
    serializer_class = RTO_DetailsSerializer