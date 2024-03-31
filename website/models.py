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

class RFReportDataSpecific(models.Model): #making a seperate table to hold sector and band specific data with the sitename as the foreign key
    site_alpha = models.CharField(max_length=10,null=True)
    site_name = models.CharField(max_length=50, null=True)
    site_address = models.CharField(max_length=200,null=True)
    author = models.CharField(max_length=50, null=True)
    reviewer = models.CharField(max_length=50, null=True)
    approver = models.CharField(max_length=50, null=True)
    report_date = models.DateField(null=True)
    qualification = models.CharField(max_length=50, null=True)
    enable_l7 = models.CharField(max_length=50, null=True)
    enable_l18 = models.CharField(max_length=50, null=True)
    enable_l21 = models.CharField(max_length=50, null=True)
    enable_l23 = models.CharField(max_length=50, null=True)
    enable_l26 = models.CharField(max_length=50, null=True)
    enable_nr850 = models.CharField(max_length=50, null=True)
    enable_nr3500 = models.CharField(max_length=50, null=True)
    feeder_length = models.FloatField(null=True) # use the lowest antenna height
    feeder_dimension = models.FloatField(null=True)
    no_sectors = models.IntegerField(null=True)
    sector_type = models.CharField(max_length=50, null=True) #directive, omni, paging,LoRa, eMDR
    # this will come up in a different page, above are common for site
    sector1_azimuth_range = models.CharField(max_length=50, null=True)
    sector1_azimuth = models.IntegerField(null=True)
    sector2_azimuth_range = models.CharField(max_length=50, null=True)
    sector2_azimuth = models.IntegerField(null=True)
    sector3_azimuth_range = models.CharField(max_length=50, null=True)
    sector3_azimuth = models.IntegerField(null=True)
    l7_sector_carrier_power = models.FloatField(null=True)
    l7_sector_num_of_carriers = models.IntegerField(null=True)
    l7_sector_tx_filter_type = models.FloatField(null=True)
    l7_sector_combiner_type = models.FloatField(null=True)
    l7_hardware_in_cabinet_or_not = models.BooleanField(null=True)
    l18_sector_carrier_power = models.FloatField(null=True)
    l18_sector_num_of_carriers = models.IntegerField(null=True)
    l18_sector_tx_filter_type = models.FloatField(null=True)
    l18_sector_combiner_type = models.FloatField(null=True)
    l18_hardware_in_cabinet_or_not = models.BooleanField(null=True)
    l21_sector_carrier_power = models.FloatField(null=True)
    l21_sector_num_of_carriers = models.IntegerField(null=True)
    l21_sector_tx_filter_type = models.FloatField(null=True)
    l21_sector_combiner_type = models.FloatField(null=True)
    l21_hardware_in_cabinet_or_not = models.BooleanField(null=True)
    l23_sector_carrier_power = models.FloatField(null=True)
    l23_sector_num_of_carriers = models.IntegerField(null=True)
    l23_sector_tx_filter_type = models.FloatField(null=True)
    l23_sector_combiner_type = models.FloatField(null=True)
    l23_hardware_in_cabinet_or_not = models.BooleanField(null=True)
    l26_sector_carrier_power = models.FloatField(null=True)
    l26_sector_num_of_carriers = models.IntegerField(null=True)
    l26_sector_tx_filter_type = models.FloatField(null=True)
    l26_sector_combiner_type = models.FloatField(null=True)
    l26_hardware_in_cabinet_or_not = models.BooleanField(null=True)
    nr85_sector_carrier_power = models.FloatField(null=True)
    nr85_sector_num_of_carriers = models.IntegerField(null=True)
    nr85_sector_tx_filter_type = models.FloatField(null=True)
    nr85_sector_combiner_type = models.FloatField(null=True)
    nr85_hardware_in_cabinet_or_not = models.BooleanField(null=True)
    nr35_sector_carrier_power = models.FloatField(null=True)
    nr35_sector_num_of_carriers = models.IntegerField(null=True)
    nr35_sector_tx_filter_type = models.FloatField(null=True)
    nr35_sector_combiner_type = models.FloatField(null=True)
    nr35_hardware_in_cabinet_or_not = models.BooleanField(null=True)

    


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
    quantity_in_hand = models.IntegerField(null=True)

    def __str__(self):
        return(f"{self.vendor} {self.model}")
    
class RHTable(models.Model): #store Radio hardware resource information
    type = models.CharField(max_length=50, null=True) 
    vendor = models.CharField(max_length=100, null=True) 
    model = models.CharField(max_length=100, null=True)
    usage = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=100, null=True)
    frequency_range = models.CharField(max_length=50, null=True)
    num_tx_ports = models.IntegerField(null=True)
    num_rx_ports = models.IntegerField(null=True)
    pa_power = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    dimesons = models.CharField(max_length=50, null=True)
    comments = models.CharField(max_length=100, null=True)
    quantity_in_hand = models.IntegerField(null=True)

    def __str__(self):
        return(f"{self.vendor} {self.model}")

class CombinerTable(models.Model): #store combiner/coupler information
    type = models.CharField(max_length=50, null=True) 
    vendor = models.CharField(max_length=100, null=True) 
    model = models.CharField(max_length=100, null=True)
    usage = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=100, null=True)
    insertion_loss = models.FloatField(null=True)
    comments = models.CharField(max_length=100, null=True)
    quantity_in_hand = models.IntegerField(null=True)

    def __str__(self):
        return(f"{self.vendor} {self.model}")

class FilterTable(models.Model): #store filter information
    type = models.CharField(max_length=50, null=True) 
    vendor = models.CharField(max_length=100, null=True) 
    model = models.CharField(max_length=100, null=True)
    usage = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=100, null=True)
    insertion_loss = models.FloatField(null=True)
    comments = models.CharField(max_length=100, null=True)
    quantity_in_hand = models.IntegerField(null=True)

    def __str__(self):
        return(f"{self.vendor} {self.model}")

class BBPTable(models.Model): # store baseband processing card information
    type = models.CharField(max_length=50, null=True) 
    vendor = models.CharField(max_length=100, null=True) 
    model = models.CharField(max_length=100, null=True)
    usage = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=100, null=True)
    lte_cell_capacity = models.IntegerField(null=True)
    nr_cell_capacity = models.IntegerField(null=True)
    comments = models.CharField(max_length=100, null=True)
    quantity_in_hand = models.IntegerField(null=True)

    def __str__(self):
        return(f"{self.vendor} {self.model}")
    
class MPTTable(models.Model): # store main processing and transmission card information
    ype = models.CharField(max_length=50, null=True) 
    vendor = models.CharField(max_length=100, null=True) 
    model = models.CharField(max_length=100, null=True)
    usage = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=100, null=True)
    lte_cell_capacity = models.IntegerField(null=True)
    nr_cell_capacity = models.IntegerField(null=True)
    comments = models.CharField(max_length=100, null=True)
    quantity_in_hand = models.IntegerField(null=True)

    def __str__(self):
        return(f"{self.vendor} {self.model}")
    
class FeederTable(models.Model): # store feeder information
    type = models.CharField(max_length=50, null=True) 
    vendor = models.CharField(max_length=100, null=True) 
    feeder_dimension = models.CharField(max_length=100, null=True)
    L7_loss_per_meter = models.CharField(max_length=50, null=True)
    L18_loss_per_meter = models.CharField(max_length=50, null=True)
    L21_loss_per_meter = models.CharField(max_length=50, null=True)
    L23_loss_per_meter = models.CharField(max_length=50, null=True)
    L26_loss_per_meter = models.CharField(max_length=50, null=True)
    U85_loss_per_meter = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=100, null=True)
    quantity_in_hand = models.FloatField(null=True)
    def __str__(self):
        return(f"{self.vendor} {self.model}")