from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Site, Resource, Record, PhyInfo, AntennaTable, RFReportDataCommon, RFReportDataSpecific, WorkRequest
from django.forms import ModelForm


Op_BOOP= [
    ('Yes','Yes'),
    ('No','No'),
        ]



class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    emp_number = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'T Number'}))
    mob_number = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number 027-xxxxxxxx'}))
     
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','emp_number','mob_number','password1', 'password2')


    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'User Name'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


class AddBasicInfoForm(forms.ModelForm):
    site_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Site Name", "class":"form-control"}), label="Site Name")
    site_alpha = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Site Alpha", "class":"form-control"}), label="Site Alpha")
    proposedRFS_date = forms.DateField(
         required=True, 
         widget=forms.widgets.DateInput(format="%Y-%m-%d", attrs={"type": "date","class":"form-control"}),
         input_formats=["%Y-%m-%d"],
         label="Planned Date"
         )
    transportable_cow = forms.CharField(required=True,  widget=forms.Select(choices=Op_BOOP,attrs={"class":"form-control"}), label="Transportable")
    cow_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Cow Name", "class":"form-control"}), label="COW Name")
    easting = forms.FloatField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Easting", "class":"form-control"}), label="Easting")
    northing = forms.FloatField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Northing", "class":"form-control"}), label="Northing")
    ground_height = forms.FloatField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Ground Height")
    address_street = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Street")
    address_suburb = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Sub Urban")
    address_city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="City")
    huawei_rnc = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Huawei RNC")
    w850_cluster = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="W850 Cluster")
    engineering_region = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Engineering Region")
    coverage_type = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Coverage Type")
    temp_site = forms.CharField(required=True,  widget=forms.Select(choices=Op_BOOP,attrs={"class":"form-control"}), label="Is this a temporary site")
    property_file_number = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Property File Number")
    deployment_engineer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Deployment Engineer")
    radio_engineer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Radio Engineer")
    add_notes = forms.CharField(widget=forms.widgets.Textarea(attrs={"placeholder":"Any additional notes", "class":"form-control"}), label="Additional Notes")

    class Meta:
          model = Site
          fields = ('site_name',
                    'site_alpha',
                    'proposedRFS_date',
                    'transportable_cow',
                    'cow_name',
                    'easting',
                    'northing',
                    'ground_height',
                    'address_street',
                    'address_suburb',
                    'address_city',
                    'huawei_rnc',
                    'w850_cluster',
                    'engineering_region',
                    'coverage_type',
                    'temp_site',
                    'property_file_number',
                    'deployment_engineer',
                    'radio_engineer',
                    'add_notes'
                    )
	
    
class PhyInfoForm(forms.ModelForm):
    site_alpha = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Site Alpha")
    frequency_band = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Frequency Band")
    vendor = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Vendor")
    sector = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Sector")
    azimuth = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Azimuth")
    antenna_height = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Antenna Height")
    electrical_tilt = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Electrical Tilt")
    mechanical_tilt = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Mechanical Tilt")
    antenna_type = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Antenna Type")
    share_antenna = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Share Antenna")
    radio_equipment = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Radio Equipment")
    split_sectors = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Split Sectors")
    main_radio_type = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Main Radio Type") 
    num_carriers = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="No of Carriers")
    capacity_card_type = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Capacity Card Type")
    num_cards = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="No of Cards")
    cabinet_suffix = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Cabinet Suffix")
    
    class Meta:
        model = PhyInfo  
        fields = '__all__' 

class RecordForm(forms.ModelForm):
    category_choices = Resource.objects.values_list('asset_name', flat=True).distinct()           
    asset_name = forms.ChoiceField(
        required=False, 
        choices=[(choice, choice) for choice in category_choices],
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    booked_by =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Name")
    from_date =  forms.DateTimeField(
         required=True, 
         widget=forms.widgets.DateTimeInput(format="%Y-%m-%dT%H:%M", attrs={"type": "datetime-local","class":"form-control"}), 
         label="From"
         )
    to_date = forms.DateTimeField(
         required=True, 
         widget=forms.widgets.DateTimeInput(format="%Y-%m-%dT%H:%M", attrs={"type": "datetime-local","class":"form-control"}),
         label="To"
         )
    # emp_number =  forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Emp Number'}))
    # phone =  forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number 027-xxxxxxxx'}))
    email =  forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    purpose =  forms.CharField(required=True, max_length=200, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Purpose'}))
    
    class Meta:
        model = Record  
        fields = ('asset_name',
                  'booked_by',
                  'from_date',
                  'to_date',
                  'email',
                  'purpose'
                  )

class BookingFilterForm(forms.Form):
    asset_name = forms.ChoiceField(choices=[], required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    from_date = forms.DateTimeField(
         required=True, 
         widget=forms.widgets.DateTimeInput(format="%Y-%m-%dT%H:%M", attrs={"type": "datetime-local","class":"form-control"}), 
         label="From"
         )
    to_date = forms.DateTimeField(
         required=True, 
         widget=forms.widgets.DateTimeInput(format="%Y-%m-%dT%H:%M", attrs={"type": "datetime-local","class":"form-control"}),
         label="To"
         )

    def __init__(self, *args, **kwargs):
        super(BookingFilterForm, self).__init__(*args, **kwargs)
        # Populate the 'resource_type' dropdown with unique values from the 'resource_type' column
        self.fields['asset_name'].choices = [(resource_type, resource_type) for resource_type in Resource.objects.values_list('asset_name', flat=True).distinct()]

class AlphaCheckForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['site_alpha']

class WorkRequestForm(forms.ModelForm):
    requesting_engineer = forms.ChoiceField(choices=[],widget=forms.Select(attrs={'class': 'form-control'}), label="Requesting Engineer")
    assigned_engineer = forms.ChoiceField(choices=[],widget=forms.Select(attrs={'class': 'form-control'}), label="Assigned Engineer")
    allocated_hours = forms.FloatField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Estimated Completion Time", "class":"form-control"}))
    start_date = forms.DateTimeField(
         required=True, 
         widget=forms.widgets.DateInput(format="%Y-%m-%d", attrs={"type": "datetime-local","class":"form-control"}),
         label="From"
         )
    end_date = forms.DateTimeField(
         required=True, 
         widget=forms.widgets.DateInput(format="%Y-%m-%d", attrs={"type": "datetime-local","class":"form-control"}),
         label="To"
         )
    work_description = forms.CharField(required=True, max_length=200, widget=forms.widgets.Textarea(attrs={"class":"form-control"}),label="Work Description") 
    subject = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"})) 
    
    def __init__(self, *args, **kwargs):
         super(WorkRequestForm, self).__init__(*args, **kwargs)
         #Populate the 'resource_type' dropdown with unique values from the 'resource_type' column
         self.fields['requesting_engineer'].choices = [(name, name) for name in User.objects.values_list('username', flat=True).distinct()]
         self.fields['assigned_engineer'].choices = [(name, name) for name in User.objects.values_list('username', flat=True).distinct()]
        
    class Meta:
        model = WorkRequest
        fields = '__all__'

class RFReportConfigurationForm(forms.ModelForm):
    class Meta:
        model = RFReportDataSpecific
        fields = '__all__'  # You can specify specific fields if needed
