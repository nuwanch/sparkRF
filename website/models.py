from django.db import models

# Create your models here.
#This model to make records above resource booking
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
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
    
#This model to keep information about sites    
class Site(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) 
    site_name = models.CharField(max_length=50)  
    site_alpha = models.CharField(max_length=10) 
    proposedRFS_date = models.DateField()
    transportable_cow = models.CharField(max_length=50)
    cow_name = models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.site_name} {self.site_alpha}")
    
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

