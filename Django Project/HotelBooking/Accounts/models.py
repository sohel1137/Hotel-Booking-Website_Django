
from django.contrib.auth.models import User
from django.db import models



# Create your models here.



class Categeroies(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title   


class Hotel(models.Model):
    
    Name = models.CharField(max_length=200)
    location = models.TextField()
    HotelInfo = models.TextField()
    image = models.ImageField(upload_to='image/')
    Ammount =models.IntegerField(max_length=5)
    User1 = models.CharField(max_length=100)
    upload_date = models.DateField(auto_now_add=True)
    cat=models.ForeignKey(Categeroies,on_delete=models.CASCADE)

    
    def __str__(self) :
         return f"{self.Name} - {self.location} -{self.cat}"





class HotelBooking(models.Model):
    hotel= models.ForeignKey(Hotel  , related_name="hotel_bookings" , on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_bookings" , on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    email=models.EmailField()
    
    BOOKING_TYPE = (
        ('CASH', 'Cash'),
        ('NET_BANKING', 'Net Banking'),
    )
    booking_type = models.CharField(max_length=20, choices=BOOKING_TYPE)
    
    ROOM_TYPES = (
        ('SINGLE', 'Single'),
        ('DOUBLE', 'Double'),
    )
    room_type = models.TextField( choices=ROOM_TYPES)
    
    
    def calculate_total_price(self):
       
        price_per_night = self.hotel.price  

        # Calculate the number of days between start_date and end_date
        num_days = (self.end_date - self.start_date).days

        # Calculate the total price
        total_price = num_days * price_per_night

        return total_price

    
'''
class Customer(models.Model):
    Username=models.CharField(max_length=100)
    Fisrt_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Location=models.CharField(max_length=100)
    contact=models.CharField(max_length=20)
    Password=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.Fisrt_Name
    '''

    