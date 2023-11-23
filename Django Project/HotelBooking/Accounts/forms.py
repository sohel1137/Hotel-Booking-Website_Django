from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Hotel, Categeroies, HotelBooking
from django.contrib.auth.forms import PasswordChangeForm


from django.core.exceptions import ValidationError
from datetime import timedelta, date
from django.utils import timezone
import re

# --------------------------- USer Admin Form -------------------------------------


class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    location = forms.CharField(label='Enter Location', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    contact = forms.IntegerField(label='Enter Contact', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))

    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'location', 'contact', 'password1', 'password2']
        labels = {
            'username': 'Enter Username',
            'first_name': 'Enter First Name',
            'last_name': 'Enter Last Name',
            'email': 'Enter Email',
            'location': 'Enter Location',
            'contact': 'Enter Contact',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
        }


# --------------------------- Customer Register Form -------------------------------------

class CustForm(UserCreationForm):
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Your Password'}))
    location = forms.CharField(label='Enter Location', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Location'}))
    contact = forms.IntegerField(label='Enter Contact', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Contact'}))

    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'location', 'contact', 'password1', 'password2']
        labels = {
            'username': 'Enter Username',
            'first_name': 'Enter First Name',
            'last_name': 'Enter Last Name',
            'email': 'Enter Email',
            'location': 'Enter Location',
            'contact': 'Enter Contact',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Location'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Contact'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        # Validation for contact field
        contact = cleaned_data.get('contact')
        if contact:
            pattern = r'^\d{10}$'  # Assuming you want a 10-digit number
            if not re.match(pattern, contact):
                self.add_error(
                    'contact', 'Enter a valid 10-digit contact number.')

        # Add similar validations for other fields as needed

        return cleaned_data


# --------------------------- Admin Login Form -------------------------------------

class AdminLogin(AuthenticationForm):
    username = forms.CharField(
        label='Username:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Enter Password:', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username']
        labels = {

            'password': 'Enter Password :'
        }


# --------------------------- USer Login Form ----------------------------------------------------------------------------------------------


class CustomerLogin(AuthenticationForm):
    username = forms.CharField(
        label='Username:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Enter Password:', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username']
        labels = {
            'password': 'Enter Password :'
        }


# --------------------------- Hotel Add Form ------------------------------------------------------------------------------------------------------------------


class HotelDataInfo(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['Name', 'location', 'HotelInfo', 'image', 'Ammount', 'cat']
        labels = {
            'Name': 'Enter Name',
            'location': 'Enter Location',
            'HotelInfo': 'Enter HotelInfo',
            'image': 'add Image',
            'Ammount': 'Ammount',
            'cat': 'select catogory ',
        }

        widgets = {

            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Add Hotel Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Hotel Location'}),
            'HotelInfo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Hotel Information'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'Ammount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Hotel Ammount'}),
            'cat': forms.Select(attrs={'class': 'form-control'}),
        }


# --------------------------- Category Form ---------------------------------------------------------------------------------------------------

class category(forms.ModelForm):
    class Meta:
        model = Categeroies
        fields = ['title', 'description']
        labels = {

            'title': 'Enter Name',
            'description': 'Enter Description',



        }

        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Category'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Category Description'}),

        }


# --------------------------- HotelBooking Form ---------------------------------------------------------------------------------------------

class HotelBookingForm(forms.ModelForm):
    class Meta:
        model = HotelBooking
        fields = ['start_date', 'end_date',
                  'email', 'booking_type', 'room_type']

        labels = {

            # 'hotel': 'Enter Hotel',
            # 'user': 'Enter User',

            'start_date': 'Enter Booking Date',
            'end_date': 'Enter Exit Date',
            'email': 'Enter Your Email',
            'booking_type': 'Enter Booking Type ',
           
        }

        widgets = {

            # 'hotel': forms.Select(attrs={'class': 'form-control'}),
            # 'user': forms.Select(attrs={'class': 'form-control'}),

            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'booking_type': forms.Select(attrs={'class': 'form-control'}),
            'room_type': forms.Select(attrs={'class': 'form-control'}),

        }

        
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # Validate start date
        if start_date and start_date < timezone.now().date():
            raise ValidationError("Start date cannot be in the past")

        # Validate end date
        if end_date and end_date < timezone.now().date():
            raise ValidationError("End date cannot be in the past")

        # Validate the duration (e.g., not exceeding 10 days)
        if start_date and end_date and (end_date - start_date).days > 10:
            raise ValidationError("Booking duration cannot exceed 10 days")

        
    
    


# --------------------------- User Update Profile ------------------------------------------------------------------------------------------


class CustUpdate(UserCreationForm):
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
        labels = {
            'username': 'Enter Username',
            'first_name': 'Enter First Name',
            'last_name': 'Enter Last Name',
            'email': 'Enter Email',

        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),

        }

        def clean_first_name(self):
            first_name = self.cleaned_data.get('first_name')
            if any(char.isdigit() for char in first_name):
                raise ValidationError("First name cannot contain numbers")
            return first_name

        def clean_last_name(self):
            last_name = self.cleaned_data.get('last_name')
            if any(char.isdigit() for char in last_name):
                raise ValidationError("Last name cannot contain numbers")
            return last_name

        def clean_contact(self):
            contact = self.cleaned_data.get('contact')
            if len(str(contact)) != 10 or not str(contact).isdigit():
                raise ValidationError("Contact must be a ten-digit number")
            return contact


# ----------------------------- Update Booking -------------------------------------------------------------------------------------------------


class UpdateBooking(forms.ModelForm):
    class Meta:
        model = HotelBooking
        fields = ['start_date', 'end_date', 'booking_type', 'room_type']

        labels = {

            # 'hotel': 'Enter Hotel',
            # 'user': 'Enter User',

            'start_date': 'Enter Booking Date',
            'end_date': 'Enter Exit Date',
            'booking_type': 'Enter Booking Type ',
            'room_type': 'Select Your Room Booking Type ',

        }

        widgets = {

            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'booking_type': forms.TextInput(attrs={'class': 'form-control'}),
            'room_type': forms.Select(attrs={'class': 'form-control'})
        }


# # ------------------------------------ User Chnage Password ------------------------------------------------------------------------------


# class serChangePassword(PasswordChangeForm):
#     old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# #------------------------------------------------------------------------------------------------------------------------------------------
