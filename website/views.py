from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddBasicInfoForm
from .models import Resource, Site
import pandas as pd
from django.http import HttpResponse
import xlsxwriter
from io import BytesIO


# Create your views here.
def home(request):
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


def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def register_user(request):
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

def customer_record(request,pk):
    if request.user.is_authenticated:
        # Look up records
        customer_record = Site.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    
def delete_record(request, pk):
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
				messages.success(request, "Record Added...")
				return redirect('home')
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

        df.to_excel(path_or_buf=response,sep=',',float_format='%.2f',index=False,decimal=",")
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

            # Write data to the worksheet
        worksheet.write('A10', current_site.site_alpha)
        worksheet.write('B10', current_site.site_name)
        worksheet1.write('C23', current_site.proposedRFS_date)
        worksheet1.write('D25', current_site.cow_name)


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
    

