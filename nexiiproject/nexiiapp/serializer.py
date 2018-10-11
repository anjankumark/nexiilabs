from rest_framework import serializers
from .models import RTO_Details

class RTO_DetailsSerializer(serializers.ModelSerializer):
	 class Meta():
	 	model=RTO_Details
	 	fields='__all__'