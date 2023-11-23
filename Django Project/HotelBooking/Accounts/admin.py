from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display=['id','Name','location','HotelInfo','image','Ammount','User1','upload_date']


@admin.register(HotelBooking)
class HotelBookingAdmin(admin.ModelAdmin):
    list_display=['id','start_date','end_date','booking_type','room_type']






@admin.register(Categeroies)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','title','description']

    