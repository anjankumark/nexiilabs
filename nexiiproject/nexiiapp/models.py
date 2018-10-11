from django.db import models

# Create your models here.
class RTO_Details(models.Model):
  id = models.AutoField(primary_key=True)
  vehicle_name=models.CharField(max_length=100)
  customer_name=models.CharField(max_length=100,unique=True)
  reg_number=models.IntegerField()
  validity = models.DateField()
  vehicle_type=models.CharField(max_length=40)
  order_number=models.PositiveSmallIntegerField()
  
  class Meta:
	    managed = True
	    db_table = 'rto_details'

  def __str__(self):
      return self.name