from django.db import models
from django.contrib.auth.models import User


# Create your models here.
   
#This model is to keep basic information about sites    
class Site(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) 
    site_name = models.CharField(max_length=50)  
    site_alpha = models.CharField(max_length=10) 
    proposedRFS_date = models.DateField()
    transportable_cow = models.CharField(max_length=50)
    cow_name = models.CharField(max_length=100)
    easting = models.FloatField(null=True)
    northing = models.FloatField(null=True)
    ground_height = models.FloatField(null=True)
    address_street = models.CharField(max_length=100, null=True)
    address_suburb = models.CharField(max_length=100, null=True)
    address_city = models.CharField(max_length=100, null=True)
    huawei_rnc = models.CharField(max_length=10, null=True)
    w850_cluster = models.CharField(max_length=10, null=True)
    engineering_region = models.CharField(max_length=100, null=True)
    coverage_type = models.CharField(max_length=100, null=True)
    temp_site = models.CharField(max_length=10, null=True)
    property_file_number = models.CharField(max_length=100, null=True)
    deployment_engineer = models.CharField(max_length=100, null=True)
    radio_engineer = models.CharField(max_length=100, null=True)
    add_notes = models.CharField(max_length=250, null=True)

    def __str__(self):
        return(f"{self.site_name} {self.site_alpha}")
    
#This model is to keep physical arrangment information of a site
class PhyInfo(models.Model):
    site_alpha = models.CharField(max_length=10)
    frequency_band = models.CharField(max_length=10)
    vendor =  models.CharField(max_length=15)
    sector =  models.IntegerField()
    azimuth =  models.IntegerField()
    antenna_height =  models.FloatField()
    electrical_tilt =  models.IntegerField()
    mechanical_tilt = models.IntegerField()
    antenna_type =  models.CharField(max_length=50)
    share_antenna =  models.CharField(max_length=10)
    radio_equipment = models.CharField(max_length=20)
    split_sectors = models.CharField(max_length=10)
    main_radio_type = models.CharField(max_length=20)
    num_carriers = models.IntegerField()
    capacity_card_type = models.CharField(max_length=20)
    num_cards = models.IntegerField()
    cabinet_suffix = models.CharField(max_length=20) 

    def __str__(self):
        return(f"{self.site_alpha} {self.frequency_band}")

 #This model is to keep physical arrangment information of a 


#------------------This is for resource booking --------------------------------------    
#This model is to maintain resources    
class Resource(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    asset_name = models.CharField(max_length=50)
    asset_owner =  models.CharField(max_length=100)
    from_date =  models.DateTimeField(null=True)
    to_date = models.DateTimeField(null=True)
    emp_number =  models.CharField(max_length=10,null=True)
    phone =  models.CharField(max_length=50,null=True)
    email =  models.CharField(max_length=50,null=True)
    purpose =  models.CharField(max_length=200,null=True)
	
    def __str__(self):
        return(f"{self.asset_name} {self.asset_owner}")

#This model to make records above resource booking
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    asset_name = models.CharField(max_length=50)
    booked_by =  models.CharField(max_length=100)
    from_date =  models.DateTimeField(null=True)
    to_date = models.DateTimeField(null=True)
    emp_number =  models.CharField(max_length=10,null=True)
    phone =  models.CharField(max_length=50,null=True)
    email =  models.CharField(max_length=50,null=True)
    purpose =  models.CharField(max_length=200,null=True)
	
    def __str__(self):
        return(f"{self.asset_name} {self.booked_by}")
    


 