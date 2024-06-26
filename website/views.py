from urllib import request
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, AddBasicInfoForm, PhyInfoForm, RecordForm, BookingFilterForm, AlphaCheckForm, WorkRequestForm, RFReportConfigurationStep1Form, RFReportConfigurationStep2Form
from .models import Resource, Site, PhyInfo, Record, WorkRequest, RFReportDataSpecific
from django.contrib.auth.models import User
import pandas as pd
from django.http import HttpResponse
import xlsxwriter
from io import BytesIO
from django.core.exceptions import ValidationError


# Create your views here.

# def create_resource(request): # this is to create resources but I'm going to keep it for the admin, will remove in future
#     if request.method == 'POST':
#         form = ResourceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_url')  # Redirect to a success page
#     else:
#         form = ResourceForm()

    # return render(request, 'create_resource.html', {'form': form})

#Page administration related

def home(request): # this is the home login page
    records = Site.objects.all()
    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!!")
            return redirect('home')
        else:
            messages.success(request, "There was an error in logging in !!, Please Try Again")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):# to logout user
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def register_user(request): # user registration
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']    
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
        else:
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {})

#Resource booking related
@login_required
def book_resource(request): # create booking
    # user = request.user
    # context = {'booked_by':f"{user.first_name}{user.last_name}",'email': user.email}
    user = request.user
    initial_data = {'booked_by':user.username, 'email': user.email}
    if request.method == "POST":
        form = RecordForm(request.POST, initial=initial_data)
        if form.is_valid():
            new_booking_start = form.cleaned_data['from_date']
            new_booking_end = form.cleaned_data['to_date']
            try:
                check_overlapping_bookings(form.cleaned_data['asset_name'], new_booking_start, new_booking_end)
            except ValidationError as e:
                form.add_error(None, e.message)
                return render(request, 'book_resource.html', {'form': form})
            book_resource = form.save(commit=False)
            book_resource.user = user
            book_resource.save()
            messages.success(request, "Booking Confirmed...")
            render(request, 'testdata.html', initial_data)
    else:
        form = RecordForm(initial=initial_data) 
    return render(request, 'book_resource.html', {'form': form})

def booking_record(request,pk): # to view specific resource booking and alter. 
    if request.user.is_authenticated:
        # Look up records
        booking_record = Record.objects.get(id=pk)
        return render(request, 'booking_record.html', {'booking_record':booking_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')

def common_booking_view(request): # to filter resource and time period before make booking
    if request.method == 'POST':
        form = BookingFilterForm(request.POST)
        if form.is_valid():
            resource_type = form.cleaned_data['asset_name']
            start_date = form.cleaned_data['from_date']
            end_date = form.cleaned_data['to_date']

            # Perform filtering based on user inputs
            bookings = Record.objects.filter(
                asset_name = resource_type,
                from_date__range=[start_date, end_date]
            )

            return render(request, 'filtered_bookings.html', {'bookings': bookings, 'form': form})
    else:
        form = BookingFilterForm()

    return render(request, 'filtered_bookings.html', {'form': form})

def view_bookings(request): # to show bookings for specific resource
    if request.user.is_authenticated:
        # Look up records
        bookings = Record.objects.all()
        return render(request, 'view_resource.html', {'bookings':bookings})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')

def request_record(request,pk): # to view specific work order  and alter. 
    if request.user.is_authenticated:
        # Look up records
        request_record = WorkRequest.objects.get(id=pk)
        # work_request = get_object_or_404(WorkRequest, pk=pk)
        return render(request, 'request_record.html', {'request_record':request_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')  
     
def update_booking(request,pk): # to update specific booking
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = RecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_booking_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
      
def delete_booking(request,pk): #to delete a booking
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')

def is_overlapping(existing_start, existing_end, new_start, new_end): #checking booking overlapping
    return (new_start < existing_end) and (existing_start < new_end)

def check_overlapping_bookings(resource, new_start, new_end): #main function for checking booking overlapping
    existing_bookings = Record.objects.filter(asset_name=resource)

    for booking in existing_bookings:
        if is_overlapping(booking.from_date, booking.to_date, new_start, new_end):
            raise ValidationError("Booking overlaps with an existing reservation.")
        
def work_request_list(request):
    if request.user.is_authenticated:
        # Look up records
        requests = WorkRequest.objects.all()
        return render(request, 'work_request_list.html', {'requests':requests})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')

def create_work_request(request):
    if request.method == 'POST':
        form = WorkRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('work_request_list')
    else:
        form = WorkRequestForm()

    return render(request, 'create_work_request.html', {'form': form})

#RF data preparation related
def reserve_alphacode(request): # alpha code reservation, self verification
    if request.method == 'POST':
        form = AlphaCheckForm(request.POST)
        if form.is_valid():
            # Check for the existence of the product name before saving
            site_alpha = form.cleaned_data['site_alpha']
            if Site.objects.filter(site_alpha=site_alpha).exists():
                messages.success(request, "This site alpha is already taken. Please choose a different one.")
                # form.add_error('site_alpha', '')
            else:
                # Save the form if the product name is unique
                form.save()
                messages.success(request, "This site alpha is available to use.")
                return redirect('reserve_alphacode')  # Redirect to the product list or any other view
                
    else:
        form =  AlphaCheckForm()

    return render(request, 'alpha_checker.html', {'form':form})

def view_siteinfo(request): # view total site info
    if request.user.is_authenticated:
        # Look up records
        records = Site.objects.all()
        return render(request, 'view_sites.html', {'records':records})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')

def customer_record(request,pk): # to show specific site information
    if request.user.is_authenticated:
        # Look up records
        customer_record = Site.objects.get(site_alpha=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    
def delete_record(request, pk): #to delete a specific site
	if request.user.is_authenticated:
		delete_it = Site.objects.get(site_alpha=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')

def add_record(request):# tnet form 
    form = AddBasicInfoForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Basic information Added...")
                return redirect('add_phy_info')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
    # site = get_object_or_404(Site, site_alpha=site_alpha)
    # if request.method == 'POST':
    #     form = AddBasicInfoForm(request.POST, instance=site)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('add_phy_info')  # Implement site_detail view as needed
    # else:
    #     form = AddBasicInfoForm(instance=site)
    # return render(request, 'add_record.html', {'form': form})

def update_record(request, sitealpha):
	if request.user.is_authenticated:
		current_record = Site.objects.get(site_alpha=sitealpha)
		form = AddBasicInfoForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'view_sites.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
      
def download(request):
    if request.user.is_authenticated:
        # Look up records
        all_records = Site.objects.all()
        df = pd.DataFrame.from_records(all_records.values())
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=filename.csv'

        df.to_csv(path_or_buf=response,sep=',',float_format='%.2f',index=False,decimal=",")
        return response
        
    else:
        messages.success(request, "You Must Be Logged In download...")
        return redirect('home')
    
def download_xl(request, pk):
    if request.user.is_authenticated:
    # Create a BytesIO object to store the Excel file
        excel_data = BytesIO()

            # Create a new workbook and add a worksheet
        workbook = xlsxwriter.Workbook(excel_data)
        worksheet = workbook.add_worksheet()
        worksheet1 = workbook.add_worksheet()

        current_site = Site.objects.get(id=pk)
        dateFormat= workbook.add_format({'num_format': 'dd/mm/yy'})
        cell_format = workbook.add_format()
        cell_format.set_pattern(1)
        cell_format.set_bg_color('pink')
        cell_format.set_align('left')

            # Write data to the worksheet
        
        worksheet.write('C5', "Site Name", cell_format)
        worksheet.write('E5', current_site.site_name, cell_format)
        worksheet.write('C6', "Site Alpha")
        worksheet.write('E6', current_site.site_alpha)
        worksheet.write('C7', "Proposed RFS/Commencement Date")
        worksheet.write('E7', current_site.proposedRFS_date, dateFormat)
        worksheet.write('C10',"Transportable (COW) - see note 3")
        worksheet.write('E10',current_site.transportable_cow)
        worksheet.write('C11',"Transportable Name")
        worksheet.write('E11', current_site.cow_name)
       

        # worksheet.write('',"")
        # worksheet.write('',)
        
        
            # Close the workbook
        workbook.close()

            # Set the BytesIO object's file pointer to the beginning
        excel_data.seek(0)

            # Create the HTTP response
        response = HttpResponse(excel_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

            # Set the file name for download
        response['Content-Disposition'] = 'attachment; filename="example.xlsx"'
        return response
    else:
        messages.success(request, "You Must Be Logged In download...")
        return redirect('home')
    
def add_phy_info(request):
	form = PhyInfoForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_phy_info = form.save()
				messages.success(request, "Sector Information Added...")
				return redirect('add_phy_info')
		return render(request, 'phy_info.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

def site_configuration_form_step1(request): # required data to create RF report step 1
    if request.method == 'POST':
        form = RFReportConfigurationStep1Form(request.POST)
        if form.is_valid():
            request.session['section_one_data'] = form.cleaned_data
            return redirect('site_configuration_form_step2')
            # form.save()
            # return redirect('success_page')  # Redirect to a success page or any other URL
    else:
        form = RFReportConfigurationStep1Form()
    return render(request, 'rf_report_configuration_form_step1.html', {'form': form})

def site_configuration_form_step2(request): # required data to create RF report step 2
    if request.method == 'POST':
        form = RFReportConfigurationStep2Form(request.POST)
        if form.is_valid():
            combined_data = dict(request.session.get('section_one_data', {}), **form.cleaned_data)
            RFReportDataSpecific.objects.create(**combined_data)
            messages.success(request, "Sector Information Added...")
            return redirect('view_siteinfo')
    else:
        form = RFReportConfigurationStep2Form()
        return render(request, 'rf_report_configuration_form_step2.html', {'form': form})

def site_update(request, site_alpha): # this is used to update site data base later from TNET form
    site = get_object_or_404(Site, site_alpha=site_alpha)
    if request.method == 'POST':
        form = AddBasicInfoForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a home
    else:
        form = AddBasicInfoForm(instance=site)
    return render(request, 'add_record.html', {'form': form})

def create_rfreport(request): # rf report creation, take necessary inputs only, data base update will be done seperately. This has the python logic to generate RF report
    pass

def create_tnet(request): # tnet form creation, take necessary inputs only
    form = AddBasicInfoForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Basic information Added...")
                return redirect('add_phy_info')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')

def create_celldata(request): #cell data creation, take necessary inputs only
    pass


def test_pass(request):
    return render(request, 'test.html')