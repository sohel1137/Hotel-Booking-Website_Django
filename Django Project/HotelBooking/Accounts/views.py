from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm,AdminLogin,CustForm,CustomerLogin,HotelBookingForm,CustUpdate,UpdateBooking
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from .forms import HotelDataInfo,category
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
from django.http import Http404 
from .mail import *
from datetime import datetime
from rest_framework import viewsets

from .serializers import HotelSerializer




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from .serializers import HotelSerializer
from django.shortcuts import render
from .forms import HotelBookingForm




from django.shortcuts import render, redirect
from .forms import HotelBookingForm
from .models import Hotel
from .serializers import HotelSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



# -------------------------------------------------------------------------------------------------------------------------------------

#        Admin Show Home Page section

#-----------------------------------------------------------------------------------------------------------------------------------------

class show(View):
    def get(self, request):

        fm = UserForm()
        new = Hotel.objects.all()

        return render(request, 'home.html', {'form': fm, 'new': new})

    def post(self, request):
        fm = UserForm()
        new = Hotel.objects.all()
        if fm.is_valid():
            fm.save()


#-----------------------------------------------------------------------------------------------------------------------------------------

#     Admin Login section to use userform creation

#-----------------------------------------------------------------------------------------------------------------------------------------


class Admin_Login(View):

    def get(self, request):
        return render(request, 'Admin_login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)

        if not User.objects.filter(username=username).exists():
            messages.warning(request, f'Username not exist')
            return redirect('Adminlogin')
        elif user == None:
            messages.info(request, f'Invalid UserName or Password')
            return redirect('Adminlogin')
        else:
            login(request, user)
            # messages.info(request, f'{username} Login Succesfully')
            return redirect('show')


#-----------------------------------------------------------------------------------------------------------------

#        Customer Login Section

#-----------------------------------------------------------------------------------------------------------------

class Customer_Login(View):

    def get(self, request):
        return render(request, 'userlogin.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)

        if not User.objects.filter(username=username).exists():
            messages.warning(request, f'Username not exist')
            return redirect('userlogin')
        elif user == None:
            messages.info(request, f'Invalid UserName or Password')
            return redirect('userlogin')
        else:
            login(request, user)
            # messages.info(request, f'{username} Login Succesfully')
            return redirect('userHome')
        

#-----------------------------------------------------------------------------------------------------------------------------------

#     customer Register

#-------------------------------------------------------------------------------------------------------------------------------------

def register_user(request):
    if request.method == 'POST':
        form = CustForm(request.POST)
        if form.is_valid():
            form.save()


            # You can also log the user in here if needed.
            # Redirect to the login page after successful registration
            return redirect('userlogin')
    else:
        form = CustForm()
    return render(request, 'user_register.html', {'form': form})


#---------------------------------------------------------------------------------------------------------------------------------------

#      logout section

#-------------------------------------------------------------------------------------------------------------------------------------

def Logout_page(request):
    logout(request)
    # messages.success(request, f' LogOut Sucessfully ')
    return redirect('userHome')




# -----------------------------------------------------------------------------------------------------------------------------------

#       Admin Add New Hotel Data

#-------------------------------------------------------------------------------------------------------------------------------

def AddHotel(request):
    if request.method == 'POST':
        fm = HotelDataInfo(request.POST, request.FILES)

        if fm.is_valid():
            task = fm.save(commit=False)
            task.User1 = request.user  # Assuming you have user authentication
            task.save()
            return redirect('show')
        else:
            # Handle the case where the form is not valid, e.g., display errors
            # You can customize this part based on your requirements
            error_message = "Form is not valid. Please check your inputs."
            return render(request, 'Admin_AddHotel.html', {'forms': fm, 'error_message': error_message})
    else:
        fm = HotelDataInfo()
        m = Hotel.objects.all()

        return render(request, 'Admin_AddHotel.html', {'forms': fm, 'm': m})

   
#----------------------------------------------------------------------------------------------------------------------------------------

#  admin can handle this features we can delete invoked data

#----------------------------------------------------------------------------------------------------------------------------------------

login_required(login_url='Adminlogin')
def deleteh(request,id):
    if request.method=='POST':
        print(id)
        form_data=Hotel.objects.get(id=id)
        form_data.delete()
        # messages.success(request, f' Data Deletes Sucessfully ')
        return redirect('show')
    


#-----------------------------------------------------------------------------------------------------------------------------------------

# Admin Can update Hotel Data

#-----------------------------------------------------------------------------------------------------------------------------------------

@login_required(login_url='Adminlogin')
def updateHotelData(request, id):

    if request.method == "POST":
        
        pi = Hotel.objects.get(id=id)

        fm = HotelDataInfo(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            # messages.success(request, f' Data Update Sucessfully ')
            return redirect('show')
    else:
        pi = Hotel.objects.get(id=id)
        fm = HotelDataInfo(instance=pi)

    return render(request, 'Admin_update.html', {'form': fm})



#-------------------------------------------------------------------------------------------------------------------------------------------

# show all click on image to show data to click image

#-------------------------------------------------------------------------------------------------------------------------------------------

def showalldata(request, id):
    form = Hotel.objects.filter(id=id)
    return render(request, 'view.html', {'form': form})



#------------------------------------------------------------------------------------------------------------------------------------------

# Admin can click on card to show card data 

#--------------------------------------------------------------------------------------------------------------------------------------------

def AdminData(request, id):
    form = Hotel.objects.filter(id=id)
    return render(request, 'AdminView.html', {'form': form})



#---------------------------------------------------------------------------------------------------------------------------------------

# user Search any hotel Name

#---------------------------------------------------------------------------------------------------------------------------------------------

def search(request):
    if request.method == 'POST':
        form = HotelBookingForm()
        user = request.POST['search']
        x = Hotel.objects.filter(Name__contains=user)
        return render(request, 'search.html', {'x': x,'form':form})
    


class HotelSearchAPIView(APIView):
    def get(self, request):
        user_query = request.GET.get('search', '')
        hotels = Hotel.objects.filter(Name__contains=user_query)
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request):
        form = HotelBookingForm()
        user_query = request.POST.get('search', '')
        hotels = Hotel.objects.filter(Name__contains=user_query)
        serializer = HotelSerializer(hotels, many=True)
        return render(request, 'search.html', {'x': hotels, 'form': form, 'api_data': serializer.data})


@api_view(['GET', 'POST'])
def search(request):
    form = HotelBookingForm()

    if request.method == 'POST':
        user_query = request.POST.get('search', '')
        hotels = Hotel.objects.filter(Name__contains=user_query)
        serializer = HotelSerializer(hotels, many=True)
        return render(request, 'search.html', {'x': hotels, 'form': form, 'api_data': serializer.data})
    else:
        return redirect('hotel-search-api')  # Redirect to the API endpoint for GET requests


#---------------------------------------------------------------------------------------------------------------------------------------------

# Admin Categrory View To Show All Category Data

#-------------------------------------------------------------------------------------------------------------------------------------------

def category_view(request):
    category_new = Categeroies.objects.all()
    new = Hotel.objects.all()
    print(category_new)
    context = {'category_new': category_new, 'new': new}

    return render(request, 'home.html', context)



#---------------------------------------------------------------------------------------------------------------------------------------------

# Admin click on category to show result with categroy

#-------------------------------------------------------------------------------------------------------------------------------------------


def click_view(request,id):
    category_new = Categeroies.objects.all()
    new = Hotel.objects.filter(cat=id)
    context = {'category_new': category_new, 'new': new}
    return render(request, 'home.html', context)



#---------------------------------------------------------------------------------------------------------------------------------------------

#   Footer Section

#-------------------------------------------------------------------------------------------------------------------------------------------


def About(request):
    return render(request, 'about.html')


def Services(request):
    return render(request, 'service.html')


def tersms(request):
    return render(request, 'terms.html')


#-------------------------------------------------------------------------------------------------------------------------------------

# This Function is used to admin a new category

#----------------------------------------------------------------------------------------------------------------------------------------

def catadd(request):
    if request.method == 'POST':
        form = category(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = category()
    return render(request, 'category.html', {'form': form})



# *******************************************************************************************************************************************

#   User Home Page show Data

#-------------------------------------------------------------------------------------------------------------------------------------------


class UserHome(View):

    def get(self, request):

        fm = UserForm()
        new = Hotel.objects.all()

        return render(request,'user_home.html', {'form': fm, 'new': new})

    def post(self, request):
        fm = UserForm()
        new = Hotel.objects.all()
        if fm.is_valid():
            fm.save()
            return redirect('userHome')







#---------------------------------------------------------------------------------------------------------------------------------------------

# user Categrory View To Show All Category Data

#-------------------------------------------------------------------------------------------------------------------------------------------



def user_categoryview(request):
    category_new = Categeroies.objects.all()
    new = Hotel.objects.all()
    print(category_new)
    context = {'category_new': category_new, 'new': new}

    return render(request, 'user_home.html', context)



#---------------------------------------------------------------------------------------------------------------------------------------------

# User Click on card to show Category Result 

#-------------------------------------------------------------------------------------------------------------------------------------------



def userclick_view(request, id):
    category_new = Categeroies.objects.all()
    new = Hotel.objects.filter(cat=id)
    context = {'category_new': category_new, 'new': new}
    return render(request, 'user_home.html', context)




#---------------------------------------------------------------------------------------------------------------------------------------------

# This Features use only on Admin Can show All Register Data

#-------------------------------------------------------------------------------------------------------------------------------------------


def Userdata(request):
    form= CustForm()
    m = User.objects.all()

    return render(request,'userdata.html',{'form':form,'m':m})
    


#---------------------------------------------------------------------------------------------------------------------------------------------

# Email Sending section

#-------------------------------------------------------------------------------------------------------------------------------------------



'''

def generate_verification_code():
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for i in range(16))

def send_verification_email(user):
    code = generate_verification_code()
    EmailVerification.objects.create(user=user, code=code)
    subject = 'Email Verification'
    message = f'Your verification code is: {code}'
    send_mail(subject, message, 'Your Email Id', [user.email])

'''


#---------------------------------------------------------------------------------------------------------------------------------------------

# User Hotel Booking Section

#-------------------------------------------------------------------------------------------------------------------------------------------


# @login_required(login_url='userlogin')
class HotelBookingView(View):
    def get(self, request,id):
        hotel = get_object_or_404(Hotel, id=id)
        
        if request.user.is_authenticated:
            
            return render(request, 'Booking.html', {'hotel': hotel})
        else:            
            return redirect('userlogin') 
                
    def post(self, request,id):
        hotel = get_object_or_404(Hotel, id=id) 
      
        
        if request.user.is_authenticated:           
            form = HotelBookingForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.hotel = hotel
                booking.user = request.user
                booking.save()

                
                email = request.POST.get("email", "")
                username = request.POST.get("username", "")
                start_date = request.POST.get("start_date", "")
                end_date = request.POST.get("end_date", "")
                room_type = request.POST.get("room_type", "")
                booking_type = request.POST.get("booking_type", "")
           

                # Now you can use the values without causing a MultiValueDictKeyError
                send_mail(email,username, start_date, end_date, room_type, booking_type)

                
                # email=request.POST["email"]
              
                # start_date = request.POST["start_date"]
                # end_date= request.POST["end_date"]
                # room_type = request.POST["room_type"]
                # booking_type = request.POST["booking_type"]
                # Ammount = request.POST("Ammount")

                

                # send_mail(email,start_date,end_date,room_type,booking_type,Ammount)
           
                return redirect('Userbookingdata')                         
            else:    
                        
                return render(request, 'Booking.html', {'hotel': hotel, 'form': form})
        else:           
            return redirect('userlogin')  




#---------------------------------------------------------------------------------------------------------------------------------------------

# This section will be use to show all booking data to admin Panel

#-------------------------------------------------------------------------------------------------------------------------------------------


def Bookingdata(request):
    form= HotelBookingForm()
    m = HotelBooking.objects.all()

    return render(request,'BookingData.html',{'form':form,'m':m})
    





#---------------------------------------------------------------------------------------------------------------------------------------------

# User Profile Update

#-------------------------------------------------------------------------------------------------------------------------------------------



def UpdateUserData(request):

    if request.method == 'POST':
        form = CustUpdate(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Profile updated successfully')
            return redirect('userHome')
        else:
            messages.error(request, 'Error updating your profile. Please correct the errors below.')
    else:
        form = CustUpdate(instance=request.user)
    
    return render(request, 'UpdateUserData.html', {'form': form})




#---------------------------------------------------------------------------------------------------------------------------------------------

# show User Profile

#-------------------------------------------------------------------------------------------------------------------------------------------

class UserProfile(View):
        def get(self,request):
            form=User.objects.get(pk=request.user.pk)

            m=CustForm(instance=form)
            return render(request,'userprofile.html',{"form":form,"m":m})
        
     


#---------------------------------------------------------------------------------------------------------------------------------------------

# show Booking Data only user

#-------------------------------------------------------------------------------------------------------------------------------------------
        
class UserBookingData(View):
    def get(self,request,*args,**kwargs):
        user_booking=HotelBooking.objects.filter(user=request.user)

        if user_booking.exists():
            form=HotelBookingForm(instance=request.user)
            return render(request, 'userbooking.html',{'form':form,'m':user_booking})
        else:
            # if no bookings found  for the current user Login to throw message
            messages=" Your Booking Is Empty."
            return render(request,"userbooking.html",{'message':messages})
        


#---------------------------------------------------------------------------------------------------------------------------------------------

# Cancel Booking

#-------------------------------------------------------------------------------------------------------------------------------------------
        

def CancelBooking(request,id):
    if request.method=='POST':
        form=HotelBooking.objects.filter(id=id)
        form.delete()

        
        # email = request.POST.get("email", "")
        # username = request.POST.get("username", "")
        # start_date = request.POST.get("start_date", "")
        # end_date = request.POST.get("end_date", "")
        # room_type = request.POST.get("room_type", "")
        # booking_type = request.POST.get("booking_type", "")
        # Ammount = request.POST.get("Ammount", "")

        # # Now you can use the values without causing a MultiValueDictKeyError
        # send_CancelMail(email,username, start_date, end_date, room_type, booking_type, Ammount)

        




        # messages.success(request, f' Data Deletes Sucessfully ')
        return redirect('Userbookingdata')
    



#---------------------------------------------------------------------------------------------------------------------------------------------

# Update Booking User

#-------------------------------------------------------------------------------------------------------------------------------------------
        


def updateBookingUser(request,id):

        if request.method == "POST":
            pi = HotelBooking.objects.get(id=id)

            fm = UpdateBooking(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                # messages.success(request, f'Booking Data Update Sucessfully ')
                return redirect('show')
        else:
            pi = HotelBooking.objects.get(id=id)
            print(pi)
            fm = UpdateBooking(instance=pi)

        return render(request, 'UpdateBooking.html', {'form': fm})




#---------------------------------------------------------------------------------------------------------------------------------------------

#  change Password User

#-------------------------------------------------------------------------------------------------------------------------------------------
        




# def ChangePassword(request):

#     if request.method == 'POST':
#         form =UserChangePassword(user=request.user, data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important for maintaining the user's session
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('userprofile')  # Redirect to user's profile or desired page after password change
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = UserChangePassword(user=request.user)
#     return render(request,'userchangepassword.html', {'form': form})
    



#---------------------------------------------------------------------------------------------------------------------------------------------

#  Admin Cancel Booking to check available rooms

#-------------------------------------------------------------------------------------------------------------------------------------------
        

def AdminCancelBooking(request,id):
    if request.method=='POST':
        form=HotelBooking.objects.filter(id=id)
        form.delete()
        messages.success(request, f' Data Deletes Sucessfully ')
        return redirect('BookingData')
    



#---------------------------------------------------------------------------------------------------------------------------------------------

#  Admin Delete Data To Register Data

#-------------------------------------------------------------------------------------------------------------------------------------------



def AdminUSerDelete(request,id):
    if request.method=='POST':
        form=User.objects.filter(id=id)
        form.delete()
        messages.success(request, f' Data Deletes Sucessfully ')
        return redirect('userdata')
    




def calculate_total_price(start_date, end_date,Ammount):
   
    total_price = Ammount 
    return total_price



# def HoteldataView1(request,id):
#      if request.method == "POST":
#             pi = HotelBooking.objects.get(id=id)

#             fm = HotelBookingForm(request.POST,instance=pi)
#             if fm.is_valid():
#                 fm.save()
#                 # messages.success(request, f'Booking Data Update Sucessfully ')
#                 return redirect('show')
#             else:
#                 pi = HotelBooking.objects.get(id=id)
#                 print(pi)
#                 fm = HotelBookingForm(instance=pi)

