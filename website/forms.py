from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Site, Resource, Record

Op_BOOP= [
    ('Yes','Yes'),
    ('No','No'),
        ]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    emp_number = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'T Number'}))
     
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','emp_number', 'password1', 'password2')


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
    proposedRFS_date = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Planned Date", "class":"form-control"}), label="Planned Date")
    transportable_cow = forms.CharField(required=True, widget=forms.Select(choices=Op_BOOP), label="Transportable")
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
    temp_site = forms.CharField(required=True,  widget=forms.Select(choices=Op_BOOP), label="Is this a temporary site")
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
	
    
      
