from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import csv
from django.shortcuts import render, redirect
from capstone_app_1.form1 import CSVUploadForm

from .models import StudentLoginDetails
from django.contrib.auth.decorators import user_passes_test


from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_superuser


def home(request):
    # check to see if logging in
    if request.method == 'POST':
        student_id = request.POST['student_id']
        email = request.POST['email']
        password = request.POST['password']
        user=authenticate(request,student_id='student_id',email='email',password='password')
        if user is not None:
            login(request,user)
            messages.success(request,'You have been login')
           # return redirect('update_password')
        else:
            messages.success("there is some errors")
            return redirect('home')
    else:
        return render(request,'home.html')    
def logout_user(request):
    logout(request)
    messages.success(request,'You have been Logged out.....')
    return  redirect('home')



@user_passes_test(is_admin)
def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            
            # Read CSV data directly from the POST data
            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
            
            # Skip header row
            next(csv_data)
            
            # Save CSV data to the database
            for row in csv_data:
                student_id, email, password = row
                StudentLoginDetails.objects.create(
                    student_id=student_id,
                    email=email,
                    password=password
                )
            
            return redirect('success')  # Redirect to success page
    else:
        form = CSVUploadForm()
    
    return render(request, 'upload_csv.html', {'form': form})
