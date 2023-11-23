"""
URL configuration for HotelBooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .import views
# from .views import HotelSearchAPIView

from .views import HotelSearchAPIView, search
urlpatterns = [
    path('api/search/', HotelSearchAPIView.as_view(), name='hotel-search-api'),
    path('search/', search, name='hotel-search'),

    

    
    
    
    path('about/',views.About,name='about'),
    path('service/',views.Services,name='service'),
    path('terms/',views.tersms,name='terms'),
    
    
    

    

    # Admin

    path('show/',views.category_view,name='show'),
    path('cat/<int:id>/',views.userclick_view,name='cat'),


    path('Adminlogin/',views.Admin_Login.as_view(),name='Adminlogin'),
    path('register/',views.register_user,name='register'),
    path('logout/',views.Logout_page,name='logout'),
    path('AddHotel/',views.AddHotel,name='AddHotel'),
    path('deleteh/<int:id>/',views.deleteh,name='deleteh'),
    path('view/<int:id>/',views.showalldata,name='view'),
    path('search/',views.search,name='search'),

    
    # path('api/search/', HotelSearchAPIView.as_view(), name='hotel-search-api'),

    path('<int:id>/',views.updateHotelData,name='update'),
    path('catgory/',views.catadd,name='catgory'),

    path('BookingData/',views.Bookingdata,name='BookingData'),

    
    path('AdminCancelBooking/<int:id>/',views.AdminCancelBooking,name='AdminCancelBooking'),
    path('AdminUSerDelete/<int:id>/',views.AdminUSerDelete,name='AdminUSerDelete'),

    path('AdminData/<int:id>/',views.AdminData,name='AdminData'),

# ------------------- User --------------------------------------------------------------------------------------------------------


    
    path('',views.user_categoryview,name='userHome'),
    path('cat/<int:id>/',views.userclick_view,name='cat'),
    path('userlogin',views.Customer_Login.as_view(),name='userlogin'),

 

 
    path('userdata/',views.Userdata,name='userdata'),
   

    path('UpdateUserData',views.UpdateUserData,name='UpdateUserData'),
    path('userprofile',views.UserProfile.as_view(),name="userprofile"),

    path('Userbookingdata',views.UserBookingData.as_view(),name="Userbookingdata"),

    path('CancelBooking/<int:id>/',views.CancelBooking,name='CancelBooking'),

    path('updatebook/<int:id>/',views.updateBookingUser,name='UpdateBooking'),

    path('book-hotel/<int:id>/',views.HotelBookingView.as_view(),name='book_hotel'),
    # path('<int:id>/',views.userBooking,name='userBooking'),

   

    

]




