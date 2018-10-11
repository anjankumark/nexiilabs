from django.urls import path

from . import views

urlpatterns = [
     
    path(r'api/rto/',views.RTO_DetailsList.as_view(),name='RTO_DetailsList'),
]