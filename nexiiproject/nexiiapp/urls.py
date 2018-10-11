'''
from django.urls import path

from . import views
#for individual applications

urlpatterns = [
     
    path(r'',views.RTO_DetailsViewSet.as_view({'get':'list'}),name='RTO_DetailsViewSet'),
]
'''
