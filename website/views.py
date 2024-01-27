from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, AddBasicInfoForm, PhyInfoForm, RecordForm, ResourceForm
from .models import Resource, Site, PhyInfo, Record
from django.contrib.auth.models import User
import pandas as pd
from django.http import HttpResponse
import xlsxwriter
from io import BytesIO


# Create your views here.

def create_resource(request): # this is to create resources but I'm going to keep it for the admin, will remove in future
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = ResourceForm()

    return render(request, 'create_resource.html', {'form': form})

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

def reserve_alphacode(request): # alpha code reservation, self verification
    pass

def create_rfreport(request): # rf report creation, take necessary inputs only
    pass

def create_tnet(request): # tnet form creation, take necessary inputs only
    pass

def create_celldata(request): #cell data creation, take necessary inputs only
    pass

@login_required
def book_resource(request): # create booking
    # user = request.user
    # context = {'booked_by':f"{user.first_name}{user.last_name}",'email': user.email}
    user = request.user
    initial_data = {'booked_by':user.username, 'email': user.email}
    if request.method == "POST":
        form = RecordForm(request.POST, initial=initial_data)
        if form.is_valid():
            book_resource = form.save(commit=False)
            book_resource.user = user
            book_resource.save()
            messages.success(request, "Basic information Added...")
            render(request, 'testdata.html', initial_data)
    else:
        form = RecordForm(initial=initial_data) 
    return render(request, 'book_resource.html', {'form': form})

 
    
def booking_record(request,pk): # to view specific booking and alter. 
    if request.user.is_authenticated:
        # Look up records
        booking_record = Record.objects.get(id=pk)
        return render(request, 'booking_record.html', {'booking_record':booking_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')

 
def view_bookings(request): # to show all the bookings
    if request.user.is_authenticated:
        # Look up records
        bookings = Record.objects.all()
        return render(request, 'view_resource.html', {'bookings':bookings})
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

def view_siteinfo(request): # view total site info
    if request.user.is_authenticated:
        # Look up records
        records = Site.objects.all()
        return render(request, 'users.html', {'records':records})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')

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

def customer_record(request,pk): # specific site information
    if request.user.is_authenticated:
        # Look up records
        customer_record = Site.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    
def delete_record(request, pk): #to delete a site
	if request.user.is_authenticated:
		delete_it = Site.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')

def add_record(request):
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

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Site.objects.get(id=pk)
		form = AddBasicInfoForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
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
