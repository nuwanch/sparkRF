from django.db import models
from django.contrib.auth.models import User


# Create your models here.
   
#This model is to keep basic information about sites    
class Site(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) 
    site_name = models.CharField(max_length=50)  
    site_alpha = models.CharField(max_length=10) 
    proposedRFS_date = models.DateField(blank=True, null=True)
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
    
#This model use to take the required data to create RF report
class RFReportDataCommon(models.Model):
    site_name = models.CharField(max_length=50)  
    address_street = models.CharField(max_length=100, null=True)
    address_suburb = models.CharField(max_length=100, null=True)
    address_city = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    qualifications = models.CharField(max_length=100, null=True)
    reviewer = models.CharField(max_length=100, null=True)
    created_date = models.DateField(auto_now_add=True)
    site_type = models.CharField(max_length=100, null=True) # New,Upgraded,Roadside
    comments = models.CharField(max_length=500, null=True)

    
    def __str__(self):
        return(f"{self.site_name} {self.author}")
    

class RFReportDataSpecific(models.Model): #making a seperate table to hold sector and band specific data with the sitename as the foreign key
    site_name = models.CharField(max_length=50, null=True)
    sector_name = models.CharField(max_length=50, null=True) #first,second,third, omni, paging,LoRa, eMDR
    sector_azimuth_range = models.CharField(max_length=50, null=True)
    sector_azimuth = models.IntegerField(null=True)
    sector_band = models.CharField(max_length=50, null=True)
    sector_carrier_power = models.FloatField(null=True)
    sector_num_of_carriers = models.IntegerField(null=True)
    sector_tx_filter_loss = models.FloatField(null=True)
    sector_combiner_loss = models.FloatField(null=True)
    sector_feeder_loss = models.FloatField(null=True)

    def __str__(self):
        return(f"{self.site_name} {self.sector_name}")
    
class AntennaTable(models.Model): #store antenna information and admin can update when new antennas are introduced
    type = models.CharField(max_length=50, null=True) 
    vendor = models.CharField(max_length=100, null=True) 
    model = models.CharField(max_length=100, null=True)
    usage = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=100, null=True)
    frequency_range = models.CharField(max_length=50, null=True)
    num_low_ports = models.IntegerField(null=True)
    num_high_ports = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    dimesons = models.CharField(max_length=50, null=True) 
    band600_gain = models.FloatField(null=True)
    band700_gain = models.FloatField(null=True)
    band850_gain = models.FloatField(null=True)
    band1800_gain = models.FloatField(null=True)
    band2100_gain = models.FloatField(null=True)
    band2300_gain = models.FloatField(null=True)
    band2600_gain = models.FloatField(null=True)
    band3500_gain = models.FloatField(null=True)
    hbw = models.FloatField(null=True)
    band600_vbw = models.FloatField(null=True)
    band700_vbw = models.FloatField(null=True)
    band850_vbw = models.FloatField(null=True)
    band1800_vbw = models.FloatField(null=True)
    band2100_vbw = models.FloatField(null=True)
    band2300_vbw = models.FloatField(null=True)
    band2600_vbw = models.FloatField(null=True)
    band3500_vbw = models.FloatField(null=True)
    freq_low = models.FloatField(null=True)
    freq_high = models.FloatField(null=True)
    connectiors = models.CharField(max_length=10, null=True)
    bracket_weight = models.FloatField(null=True)
    size = models.CharField(max_length=10, null=True)
    comments = models.CharField(max_length=100, null=True)

    def __str__(self):
        return(f"{self.vendor} {self.model}")
    


class WorkRequest(models.Model): #To make work requests to engineers
    requesting_engineer = models.CharField(max_length=255)
    assigned_engineer = models.CharField(max_length=255)
    allocated_hours = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    work_description = models.TextField(max_length=255)
    subject = models.CharField(max_length=255)
    attachments = models.FileField(upload_to='media/work_request_attachments/', blank=True, null=True)

    def __str__(self):
        return f"{self.subject} - Requested by: {self.requesting_engineer.username}"



 